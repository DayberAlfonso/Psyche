"""
Callbacks module for Dash app interactivity.
"""

import plotly.graph_objects as go
from dash import Input, Output, html, State, clientside_callback

from api.sentiment import analyze_sentiment


def register_callbacks(app):
    """
    Register all callbacks with the Dash app.
    """

    @app.callback(
        [Output("result-output", "children"), Output("sentiment-chart", "figure"), Output("result-text", "children")],
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
                text=">>> ENTER TEXT TO SEE SENTIMENT VISUALIZATION",
                xref="paper", yref="paper",
                x=0.5, y=0.5, showarrow=False,
                font=dict(size=14, color="#00ffff", family="Courier New")
            )
            empty_fig.update_layout(
                xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
                yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
                plot_bgcolor="white"
            )
            empty_fig.update_layout(
                plot_bgcolor="#000000",
                paper_bgcolor="#000000"
            )
            return (
                html.Div(
                    ">>> PLEASE ENTER SOME TEXT TO ANALYZE...", 
                    style={
                        "color": "#00ffff",
                        "fontFamily": "'Courier New', monospace",
                        "textShadow": "0 0 5px #00ffff"
                    }
                ),
                empty_fig,
                ""
            )

        sentiment_label, polarity_score = analyze_sentiment(text)

        # Color coding based on sentiment (retro neon colors)
        if sentiment_label == "Positive":
            color = "#00ff00"  # Neon Green
            emoji = "😊"
            glow_color = "#00ff00"
        elif sentiment_label == "Negative":
            color = "#ff0080"  # Hot Pink
            emoji = "😞"
            glow_color = "#ff0080"
        else:
            color = "#ffff00"  # Neon Yellow
            emoji = "😐"
            glow_color = "#ffff00"

        # Create gauge chart with retro styling
        fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = polarity_score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            delta = {
                'reference': 0,
                'font': {'color': '#00ffff', 'family': 'Orbitron'}
            },
            gauge = {
                'axis': {'range': [-1, 1], 'tickcolor': '#00ffff', 'tickwidth': 2},
                'bar': {'color': color},
                'bgcolor': "#000000",
                'steps': [
                    {'range': [-1, -0.33], 'color': "#330000"},
                    {'range': [-0.33, 0.33], 'color': "#333300"},
                    {'range': [0.33, 1], 'color': "#003300"}
                ],
                'threshold': {
                    'line': {'color': "#00ffff", 'width': 4},
                    'thickness': 0.75,
                    'value': 0
                }
            },
            number = {'font': {'color': color, 'size': 20, 'family': 'Orbitron'}}
        ))

        fig.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=10, b=20),
            paper_bgcolor="#000000",
            font=dict(size=14, color="#00ffff", family="Orbitron"),
            plot_bgcolor="#000000"
        )

        result_text = f"Sentiment: {sentiment_label} {emoji} ({polarity_score:.3f})\nText: {text}"
        
        return (
            html.Div(
                [
                    html.H4(
                        f">>> SENTIMENT: {sentiment_label} {emoji} ({polarity_score:.3f})",
                        style={
                            "color": color,
                            "marginBottom": "10px",
                            "fontFamily": "'Courier New', monospace",
                            "textShadow": f"0 0 10px {glow_color}",
                            "fontWeight": "bold"
                        },
                    ),
                    html.P(
                        f'>>> TEXT: "{text}"', 
                        style={
                            "color": "#00ffff",
                            "fontSize": 14,
                            "fontFamily": "'Courier New', monospace",
                            "textShadow": "0 0 5px #00ffff"
                        }
                    ),
                ]
            ),
            fig,
            result_text
        )
    
    # Client-side callback for clipboard copy
    clientside_callback(
        """
        function(n_clicks, text_to_copy) {
            if (n_clicks && text_to_copy) {
                navigator.clipboard.writeText(text_to_copy).then(function() {
                    return "✓ Copied to clipboard!";
                }).catch(function(err) {
                    return "Failed to copy";
                });
                return "✓ Copied to clipboard!";
            }
            return "";
        }
        """,
        Output("copy-status", "children"),
        Input("copy-button", "n_clicks"),
        State("result-text", "children"),
        prevent_initial_call=True,
    )
