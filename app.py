# Import libraries
import streamlit as st
import openai
import requests
from bs4 import BeautifulSoup
from feedparser import parse as parse_rss
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import datetime
import pandas as pd
import io
from dotenv import load_dotenv
import os

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def fetch_rss_feed(feed_url, start_date, end_date, max_items=50):
    """Fetches up to max_items news title, link, and published date from an RSS feed within a date range."""
    try:
        feed = parse_rss(feed_url)
        news_items = []
        for entry in feed.entries:
            if len(news_items) >= max_items:
                break
            if hasattr(entry, 'published_parsed'):
                published_date = datetime.datetime(*entry.published_parsed[:6])
                if start_date <= published_date < (end_date + datetime.timedelta(days=1)):
                    news_item = {
                        'title': entry.title,
                        'link': entry.link,
                        'published_date': published_date
                    }
                    news_items.append(news_item)
        return news_items
    except Exception as e:
        st.error(f"Error fetching RSS feed: {e}")
        return []

def scrape_article_content(article_url):
    """Scrapes the main article content from a given URL."""
    try:
        response = requests.get(article_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        article_text = ' '.join([para.get_text() for para in paragraphs if para.get_text().strip()])
        return article_text
    except Exception as e:
        st.error(f"Error scraping article: {e}")
        return None

def analyze_sentiment(text):
    """Analyzes sentiment using TextBlob and VADER combined."""
    if not text:
        return "Neutral"
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    processed_text = ' '.join(lemmas)

    blob = TextBlob(processed_text)

    vader_analyzer = SentimentIntensityAnalyzer()
    vader_scores = vader_analyzer.polarity_scores(processed_text)

    combined_sentiment = blob.sentiment.polarity + vader_scores['compound']

    threshold = 0.2
    if combined_sentiment > threshold:
        return "Positive"
    elif combined_sentiment < -threshold:
        return "Negative"
    else:
        return "Neutral"

def generate_counter_attack_article(article_text, sentiment):
    """Generates a counter-attack news article by rephrasing content based on the sentiment."""
    prompt = f"Rewrite the following news article to present an opposing view while keeping the factual information intact. Original sentiment: {sentiment}. News article: {article_text}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that rewrites news articles to present an opposing sentiment while maintaining factual accuracy."},
            {"role": "user", "content": prompt}
        ]
    )

    counter_attack_article = response.choices[0].message['content'].strip()
    return counter_attack_article

def process_articles(news_data):
    """Processes news articles and generates counter-attack articles."""
    articles_list = []

    total_articles = len(news_data)
    progress_bar = st.progress(0)

    for i, article in enumerate(news_data):
        content = scrape_article_content(article['link'])

        if content:
            title_sentiment = analyze_sentiment(article['title'])
            content_sentiment = analyze_sentiment(content)

            if content_sentiment == "Positive" or title_sentiment == "Positive":
                overall_sentiment = "Positive"
            elif content_sentiment == "Negative" or title_sentiment == "Negative":
                overall_sentiment = "Negative"
            else:
                overall_sentiment = "Neutral"

            counter_attack_article = generate_counter_attack_article(content, overall_sentiment)
            counter_sentiment = analyze_sentiment(counter_attack_article)

            article_data = {
                'Published Date': article['published_date'],
                'Headline': article['title'],
                'Original Content': content,
                'Original Sentiment': overall_sentiment,
                'Counter Article': counter_attack_article,
                'Counter Sentiment': counter_sentiment
            }

            articles_list.append(article_data)
        else:
            st.warning(f"Content not found for article: {article['title']}")

        progress = (i + 1) / total_articles
        progress_bar.progress(progress)

    df = pd.DataFrame(articles_list)
    st.session_state['df'] = df
    return df

def main():
    st.title("News Sentiment Analysis and Counter-Attack Article Generator")

    start_date = st.date_input("Start Date", datetime.date(2024, 1, 1))
    end_date = st.date_input("End Date", datetime.date.today())

    start_date = datetime.datetime.combine(start_date, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(end_date, datetime.datetime.min.time())

    if st.button("Fetch and Process News") and 'df' not in st.session_state:
        feed_url = "https://www.livemint.com/rss/politics"
        news_data = fetch_rss_feed(feed_url, start_date, end_date)

        if news_data:
            with st.spinner("Processing articles..."):
                df = process_articles(news_data)

            st.write("\nNews Articles with Sentiment Analysis and Counter-Attack Articles:")
            st.dataframe(df)

    if 'df' in st.session_state:
        df = st.session_state['df']

        towrite = io.BytesIO()
        with pd.ExcelWriter(towrite, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
        towrite.seek(0)

        st.download_button("Download Excel", towrite, file_name="news_data_with_sentiment.xlsx")

if __name__ == "__main__":
    main()
