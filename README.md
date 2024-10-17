# News Sentiment Analysis and Counter-Attack Article Generator

This project is a web application built using Streamlit that fetches news articles from an RSS feed, analyzes their sentiment, and generates counter-attack articles. The application utilizes OpenAI's GPT-3.5 for rephrasing content while maintaining factual accuracy.

## Project Description

This project is a Streamlit web application designed to analyze news articles by fetching them from an RSS feed. It employs sentiment analysis techniques using TextBlob and VADER to determine the sentiment of article titles and content. Additionally, the application generates counter-attack articles using OpenAI's GPT-3.5, presenting opposing viewpoints while maintaining factual accuracy.

Users can specify a date range for retrieving news articles, making it easy to focus on specific events or topics. The fetched articles include titles, links, published dates, and their analyzed sentiments. After processing, users can view the original content, its sentiment, and the generated counter-attack article alongside its sentiment analysis.

The app allows users to download the results in Excel format for further analysis or record-keeping. It leverages various libraries, including BeautifulSoup for web scraping, NLTK for natural language processing, and Pandas for data handling.

This tool is particularly useful for journalists, researchers, and anyone interested in understanding media bias or exploring alternative viewpoints on current events. By combining sentiment analysis and counter-narratives, the application fosters a more nuanced understanding of news coverage.

## Features

- Fetch news articles from an RSS feed within a specified date range.
- Analyze the sentiment of article titles and contents using TextBlob and VADER.
- Generate counter-attack articles that present opposing views while preserving factual integrity.
- Download results in Excel format for further analysis.

## Technologies Used

- Python
- Streamlit
- OpenAI API
- BeautifulSoup (for web scraping)
- VADER Sentiment Analysis
- TextBlob
- NLTK (Natural Language Toolkit)
- Pandas
- Requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/news-sentiment-analysis.git
   cd news-sentiment-analysis

2.Install the required packages:
  ```bash
  pip install -r requirements.txt


3.Set up your OpenAI API key:
  ```bash
  streamlit run app.py


Open your web browser and go to http://localhost:8501 to access the application.

Enter the start and end dates to fetch news articles, then click on "Fetch and Process News".

The processed articles along with their sentiments and counter-attack articles will be displayed. You can download the results as an Excel file.


