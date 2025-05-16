import pandas as pd
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def categorize_sentiment(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    df = pd.read_csv("reviews.csv")
    df["polarity"] = df["review"].apply(analyze_sentiment)
    df["sentiment"] = df["polarity"].apply(categorize_sentiment)

    # Statistics
    sentiment_counts = df["sentiment"].value_counts()
    print("Sentiment Counts:\n", sentiment_counts)

    # Visualization
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="sentiment", palette="Set2")
    plt.title("Sentiment Analysis of Amazon Reviews")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Reviews")
    plt.show()

    # Save results
    df.to_csv("analyzed_reviews.csv", index=False)

if __name__ == "__main__":
    main()
