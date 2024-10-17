# News Sentiment Analysis and Counter-Attack Article Generator

A Streamlit web application that analyzes news article sentiments and generates counter-perspective articles using AI. The application fetches news from RSS feeds, performs sentiment analysis using multiple techniques, and creates balanced counter-narratives while maintaining factual accuracy.

## Features

- RSS feed parsing for news articles
- Web scraping of article content
- Dual sentiment analysis using TextBlob and VADER
- AI-powered counter-narrative generation using GPT-3.5
- Interactive date range selection
- Export results to Excel
- Progress tracking for article processing
- Clean and intuitive user interface

## Prerequisites

Before running this application, make sure you have Python 3.7+ installed and an OpenAI API key. You'll also need to install the required dependencies.

### Required API Keys

- OpenAI API key (for GPT-3.5 access)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/news-sentiment-analysis.git
cd news-sentiment-analysis
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to `http://localhost:8501`

3. Select your desired date range for news articles

4. Click "Fetch and Process News" to start the analysis

5. Download the results in Excel format using the "Download Excel" button

## Dependencies

- streamlit
- openai
- requests
- beautifulsoup4
- feedparser
- vaderSentiment
- textblob
- nltk
- pandas
- python-dotenv
- xlsxwriter

## Project Structure

```
news-sentiment-analysis/
│
├── app.py                 # Main application file
├── .env                   # Environment variables (create this file)
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Key Functions

- `fetch_rss_feed()`: Retrieves news articles from RSS feeds within a specified date range
- `scrape_article_content()`: Extracts article content from web pages
- `analyze_sentiment()`: Performs sentiment analysis using both TextBlob and VADER
- `generate_counter_attack_article()`: Creates counter-narrative articles using GPT-3.5
- `process_articles()`: Manages the complete workflow of article processing
- `main()`: Handles the Streamlit interface and user interactions

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT-3.5 API
- VADER and TextBlob for sentiment analysis capabilities
- Streamlit for the web application framework





