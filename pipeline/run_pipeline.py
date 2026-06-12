from ingestion.youtube_fetch_comments import fetch_comments
from processing.preprocess import clean_text
from processing.sentiment_analysis import analyze_sentiment
from database.insert_data import insert_comment
from processing.save_to_lake import save_raw

comments = fetch_comments()

print("Comments fetched:", comments)

processed_data = []

for c in comments:

    text = clean_text(c["comment"])

    sentiment, polarity = analyze_sentiment(text)

    insert_comment(c["video_id"], text, sentiment, polarity)

    processed_data.append({
        "video_id": c["video_id"],
        "comment": text,
        "sentiment": sentiment,
        "polarity": polarity
    })

# ✅ SAVE TO DATA LAKE
save_raw(processed_data)

print("Pipeline completed")