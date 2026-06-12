## Data Source

This project does not use a static dataset.

Comments are collected in real time using the YouTube Data API v3. During execution, the system fetches the latest comments from a specified YouTube video, processes them, and performs sentiment analysis on the incoming data.

### Requirements

Before running the project:

1. Create a project in Google Cloud Console.
2. Enable YouTube Data API v3.
3. Generate an API Key.
4. Add the API key to the configuration file.

```python
YOUTUBE_API_KEY = "YOUR_API_KEY"

 Features
Comment Collection
Real-time YouTube comment extraction
YouTube Data API integration
Automated comment retrieval
Continuous comment monitoring



Sentiment Analysis
Positive sentiment detection
Negative sentiment detection
Neutral sentiment detection
Text preprocessing and cleaning
NLP-based sentiment classification


Analytics & Reporting
Sentiment distribution analysis
Audience engagement monitoring
Comment volume tracking
Trend analysis
Interactive dashboards
Data Processing


Real-time data ingestion
Data cleaning and preprocessing
Automated sentiment scoring
Structured data storage

YouTube Video
      │
      ▼
YouTube Data API
      │
      ▼
Comment Extraction Layer
      │
      ▼
Data Preprocessing
      │
      ▼
Sentiment Analysis Engine
      │
      ▼
Data Storage
      │
      ▼
Streamlit Dashboard
      │
      ▼
Analytics & Visualizations


🛠️ Tech Stack
Programming Language
Python

Data Collection
YouTube Data API v3

Data Processing
Pandas
NumPy

Natural Language Processing
NLTK
TextBlob
VADER Sentiment Analyzer

Visualization Tools
Streamlit
Plotly
Matplotlib
Storage
CSV
MYSQL
