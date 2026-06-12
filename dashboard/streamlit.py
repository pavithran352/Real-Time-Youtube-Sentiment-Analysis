
import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
from streamlit_autorefresh import st_autorefresh

# Auto refresh every 10 seconds
st_autorefresh(interval=10000, key="refresh")

st.title("YouTube Comment Sentiment Dashboard")

file_path = "data_lake/raw/processed/sentiment.csv"

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:

    df = pd.read_csv(file_path)

    st.subheader("Comments Data")
    st.dataframe(df)

    # Sentiment Distribution
    st.subheader("Sentiment Distribution")
    sentiment_counts = df["sentiment"].value_counts()
    st.bar_chart(sentiment_counts)

    # Top Positive Comments
    st.subheader("Top Positive Comments")
    positive = df[df["sentiment"] == "positive"]
    st.write(positive.head(5))

    # Top Negative Comments
    st.subheader("Top Negative Comments")
    negative = df[df["sentiment"] == "negative"]
    st.write(negative.head(5))

    # Sentiment Pie Chart
    st.subheader("Sentiment Percentage")

    fig, ax = plt.subplots()
    df["sentiment"].value_counts().plot.pie(
        autopct="%1.1f%%",
        ax=ax
    )

    st.pyplot(fig)

else:
    st.warning("No data available. Run pipeline first.")