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

🚀 Key Features

🔴 Real-Time Comment Monitoring
Live YouTube comment extraction
Continuous comment collection pipeline
Dynamic sentiment updates
💬 Sentiment Analysis Engine
Positive sentiment detection
Negative sentiment detection
Neutral sentiment detection
NLP-based text processing

📊 Interactive Analytics Dashboard
Real-time sentiment distribution
Audience engagement metrics
Trend monitoring
Performance analytics


📈 Data Visualization
Sentiment pie charts
Bar chart analysis
Trend graphs
Comment volume analysis


⚡ Automated Data Processing
Comment preprocessing
Text cleaning
Sentiment scoring
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

📊 Dashboard Insights

The dashboard provides:

✅ Total Comments Processed

✅ Positive Sentiment Percentage

✅ Negative Sentiment Percentage

✅ Neutral Sentiment Percentage

✅ Audience Engagement Analysis

✅ Sentiment Trend Monitoring

✅ Comment Activity Tracking

✅ Interactive Data Visualizations

🔮 Future Enhancements
Multi-language Sentiment Analysis
Real-Time Streaming Analytics
Topic Detection
Emotion Classification
Cloud Deployment
Advanced NLP Models
