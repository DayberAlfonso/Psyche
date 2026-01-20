"""
Sentiment analysis module using TextBlob.
"""
from textblob import TextBlob


def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.
    
    Returns:
        tuple: (sentiment_label, polarity_score)
            - sentiment_label: "Positive", "Negative", or "Neutral"
            - polarity_score: float between -1.0 and 1.0
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        label = "Positive"
    elif polarity < 0:
        label = "Negative"
    else:
        label = "Neutral"
    
    return label, polarity
