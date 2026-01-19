"""
Entry point for the Psyche Sentiment Analyzer application.
Run this file to start the Dash server.
"""
from app import app


if __name__ == "__main__":
    app.run(debug=True)
