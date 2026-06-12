import csv
import os

def save_raw(data):

    os.makedirs("data_lake/raw/processed", exist_ok=True)

    file_path = "data_lake/raw/processed/sentiment.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow(["video_id","comment","sentiment","polarity"])

        for c in data:
            writer.writerow([c["video_id"], c["comment"], c["sentiment"], c["polarity"]])

    print("Data saved to sentiment.csv")