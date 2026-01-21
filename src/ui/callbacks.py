"""
Callbacks module for Dash app interactivity.
"""

import plotly.graph_objects as go
from dash import Input, Output, html

from api.sentiment import analyze_sentiment


def register_callbacks(app):
    """
    Register all callbacks with the Dash app.
    """

    @app.callback(
        [Output("result-output", "children"), Output("sentiment-chart", "figure")],
        Input("text-input", "value"),
        prevent_initial_call=True,
    )
    def update_sentiment(text):
        """
        Update the sentiment analysis result and chart in real-time as text changes.
        """
        if not text or text.strip() == "":
            empty_fig = go.Figure()
            empty_fig.add_annotation(
                text="Enter text to see sentiment visualization",
                xref="paper", yref="paper",
                x=0.5, y=0.5, showarrow=False,
                font=dict(size=16, color="#6c757d")
            )
            empty_fig.update_layout(
                xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
                yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
                plot_bgcolor="white"
            )
            return (
                html.Div(
                    "Please enter some text to analyze.", style={"color": "#6c757d"}
                ),
                empty_fig
            )

        sentiment_label, polarity_score = analyze_sentiment(text)

        # Color coding based on sentiment
        if sentiment_label == "Positive":
            color = "#28a745"  # Green
            emoji = "😊"
        elif sentiment_label == "Negative":
            color = "#dc3545"  # Red
            emoji = "😞"
        else:
            color = "#ffc107"  # Yellow
            emoji = "😐"

        # Create gauge chart
        fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = polarity_score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            delta = {'reference': 0},
            gauge = {
                'axis': {'range': [-1, 1]},
                'bar': {'color': color},
                'steps': [
                    {'range': [-1, -0.33], 'color': "#f8f9fa"},
                    {'range': [-0.33, 0.33], 'color': "#fff3cd"},
                    {'range': [0.33, 1], 'color': "#d4edda"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 0
                }
            }
        ))

        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=10, b=20),
            paper_bgcolor="white",
            font=dict(size=14)
        )

        return (
            html.Div(
                [
                    html.H4(
                        f"Sentiment: {sentiment_label} {emoji} ({polarity_score:.3f})",
                        style={"color": color, "marginBottom": "10px"},
                    ),
                    html.P(
                        f'You entered: "{text}"', style={"color": "#6c757d", "fontSize": 14}
                    ),
                ]
            ),
            fig
        )
