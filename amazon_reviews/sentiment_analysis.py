from textblob import TextBlob
import pandas as pd

df = pd.read_json("reviews.json")

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

df["sentiment"] = df["review"].apply(get_sentiment)
df.to_csv("sentiment_analysis.csv", index=False)
