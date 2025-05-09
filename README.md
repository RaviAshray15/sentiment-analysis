# Sentiment Analysis App

A real-time sentiment analysis web app built using **Python**, **Streamlit**, and **VADER**. This app analyzes any input text and classifies its sentiment as **Positive**, **Negative**, or **Neutral**, along with detailed sentiment scores.

## ----> Features

- Accepts user input via a clean Streamlit interface
- Real-time sentiment detection using **VADER SentimentIntensityAnalyzer**
- Displays compound, positive, negative, and neutral scores
- Emoji-enhanced sentiment result for a fun user experience
- Includes short explanations for score interpretation

## ----> Tech Stack

- Python 3.x
- Streamlit
- VADER (from `vaderSentiment` package)

## ----> Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/RaviAshray15/sentiment-analysis.git
cd sentiment-analysis
pip install -r requirements.txt
streamlit run app.py
