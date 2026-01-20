"""
Callbacks module for Dash app interactivity.
"""

from dash import Input, Output, State, html, callback_context

from api.sentiment import analyze_sentiment


def register_callbacks(app):
    """
    Register all callbacks with the Dash app.
    """

    @app.callback(
        Output("result-output", "children"),
        [Input("analyze-button", "n_clicks"),
         Input("text-input", "value")],
        State("real-time-toggle", "value"),
        prevent_initial_call=True,
    )
    def update_sentiment(n_clicks, text, real_time):
        """
        Update the sentiment analysis result when the button is clicked or 
        when real-time analysis is enabled and text changes.
        """
        ctx = callback_context
        triggered_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None
        
        # Only analyze on button click OR if real-time is enabled and text changed
        if triggered_id == "text-input" and not real_time:
            return html.Div(
                "Your sentiment analysis will appear here...",
                style={"color": "#6c757d"}
            )
        
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
