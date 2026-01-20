"""
Callbacks module for Dash app interactivity.
"""

from dash import Input, Output, html

from api.sentiment import analyze_sentiment


def register_callbacks(app):
    """
    Register all callbacks with the Dash app.
    """

    @app.callback(
        Output("result-output", "children"),
        Input("text-input", "value"),
        prevent_initial_call=True,
    )
    def update_sentiment(text):
        """
        Update the sentiment analysis result in real-time as text changes.
        """
        if not text or text.strip() == "":
            return html.Div(
                "Please enter some text to analyze.", style={"color": "#6c757d"}
            )

        sentiment = analyze_sentiment(text)

        # Color coding based on sentiment
        if sentiment == "Positive":
            color = "#28a745"  # Green
            emoji = "😊"
        elif sentiment == "Negative":
            color = "#dc3545"  # Red
            emoji = "😞"
        else:
            color = "#ffc107"  # Yellow
            emoji = "😐"

        return html.Div(
            [
                html.H4(
                    f"Sentiment: {sentiment} {emoji}",
                    style={"color": color, "marginBottom": "10px"},
                ),
                html.P(
                    f'You entered: "{text}"', style={"color": "#6c757d", "fontSize": 14}
                ),
            ]
        )
