# News Sentiment Analysis and Counter-Attack Article Generator

This project is a web application built using Streamlit that fetches news articles from an RSS feed, analyzes their sentiment, and generates counter-attack articles. The application utilizes OpenAI's GPT-3.5 for rephrasing content while maintaining factual accuracy.

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
