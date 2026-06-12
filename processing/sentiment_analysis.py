from transformers import pipeline

# Load sentiment model
sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text):

    result = sentiment_model(text)[0]

    sentiment = result["label"].lower()
    score = result["score"]

    if sentiment == "positive":
        polarity = score
    else:
        polarity = -score

    return sentiment, polarity