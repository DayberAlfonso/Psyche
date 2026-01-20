"""
Layout module for the Dash app UI.
"""
from dash import dcc, html
import dash_bootstrap_components as dbc


def create_layout():
    """
    Create and return the app layout.
    
    Returns:
        dash_bootstrap_components.Container: The main app layout
    """
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("Psyche, Sentiment Analysis", className="text-center mb-4"),
                html.Hr(),
            ], width=12)
        ]),
        
        dbc.Row([
            dbc.Col([
                html.Label("Enter your text:", className="mb-2"),
                dcc.Textarea(
                    id="text-input",
                    placeholder="Type your sentiment here...",
                    value="",
                    style={"width": "100%", "height": 200, "fontSize": 16},
                    className="mb-3"
                ),
            ], width=12, md=6),
            
            dbc.Col([
                html.Label("Result:", className="mb-2"),
                html.Div(
                    id="result-output",
                    children="Your sentiment analysis will appear here...",
                    style={
                        "minHeight": 200,
                        "padding": "15px",
                        "border": "2px solid #dee2e6",
                        "borderRadius": "5px",
                        "fontSize": 18,
                        "backgroundColor": "#f8f9fa"
                    },
                    className="mb-3"
                ),
            ], width=12, md=6)
        ])
    ], fluid=True, className="p-4")