from googleapiclient.discovery import build
import json
from datetime import datetime
from config.config import *

def fetch_comments():

    youtube = build("youtube", "v3", developerKey="AIzaSyCwCxf35fpTYCEBG9-qGjuKqv_LqPvyRGY")

    request = youtube.commentThreads().list(
        part="snippet",
        videoId="dQw4w9WgXcQ",
        maxResults=10
    )

    response = request.execute()

    comments = []

    for item in response["items"]:

        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

        data = {
            "video_id": "dQw4w9WgXcQ",
            "comment": comment,
            "timestamp": str(datetime.now())
        }

        comments.append(data)

    return comments