# 🛍️ Amazon Review Sentiment Analysis

## 📌 Overview
This project scrapes product reviews from **Amazon**, analyzes sentiment using **Natural Language Processing (NLP)**, and visualizes key insights. It helps understand **customer feedback trends** to make data-driven decisions.

## 🚀 Features
- **Web Scraping** → Extract Amazon reviews using **Scrapy/Selenium**.
- **Sentiment Analysis** → Classify reviews as **positive, negative, or neutral** using **TextBlob**.
- **Data Visualization** → Plot trends with **Matplotlib & Seaborn**.
- **Interactive Dashboard** → Explore insights using **Streamlit**.

## 🔧 Installation & Setup
### 1️⃣ Clone Repository
```bash
git clone https://github.com/Hari-2782/amazon_review_sentiment.git
cd amazon_review_sentiment
```
### 2️⃣ Create Virtual Environment
```bash
python -m venv scraper_env
source scraper_env/bin/activate  # Mac/Linux
scraper_env\Scripts\activate     # Windows
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run Scraper (Amazon Reviews)
```bash
scrapy crawl amazon -o reviews.json
```
### 5️⃣ Perform Sentiment Analysis
```bash
python sentiment_analysis.py
```
### 6️⃣ Start Streamlit Dashboard
```bash
streamlit run app.py
```

## 📊 Data Visualization
Key insights are presented via histograms, word clouds, and sentiment distribution graphs.
### 🔥 Future Enhancements
Integrate Deep Learning (BERT) for better sentiment accuracy.

Deploy API using FastAPI for real-time sentiment analysis.

Automate web scraping for periodic data updates.

## 📜 License
This project is licensed under MIT License.
