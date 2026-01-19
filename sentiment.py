"""
Sentiment analysis module using TextBlob.
"""
from textblob import TextBlob


def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"
