import streamlit as st
import pandas as pd

st.title("Amazon Review Sentiment Analysis")

df = pd.read_csv("sentiment_analysis.csv")
st.write(df)

st.bar_chart(df["sentiment"])

