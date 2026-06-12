import mysql.connector

def insert_comment(video_id, comment, sentiment, polarity):

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pavithran_25",
        database="youtube_sentiment"
    )

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO youtube_comments
        (video_id, comment, sentiment, polarity)
        VALUES (%s, %s, %s, %s)
    """, (video_id, comment, sentiment, polarity))

    conn.commit()
    conn.close()