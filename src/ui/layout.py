"""
Layout module for the Dash app UI.
"""
from dash import dcc, html
import dash_bootstrap_components as dbc


def create_layout():
    """
    Create and return the app layout.
    """
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("PSYCHE SENTIMENT ANALYZER", className="text-center mb-4"),
                html.Hr(style={"borderColor": "#00ffff", "borderWidth": "2px", "boxShadow": "0 0 10px #00ffff"}),
            ], width=12)
        ]),
        
        dbc.Row([
            dbc.Col([
                html.Label(
                    "ENTER YOUR TEXT:", 
                    className="mb-2",
                    style={
                        "color": "#00ffff",
                        "fontWeight": "bold",
                        "textShadow": "0 0 5px #00ffff",
                        "fontSize": "14px",
                        "letterSpacing": "1px"
                    }
                ),
                dcc.Textarea(
                    id="text-input",
                    placeholder=">>> TYPE YOUR SENTIMENT HERE...",
                    value="",
                    style={
                        "width": "100%",
                        "height": 200,
                        "fontSize": 14,
                        "fontFamily": "'Courier New', monospace",
                        "backgroundColor": "#000000",
                        "color": "#00ff00",
                        "border": "3px solid #00ffff",
                        "borderRadius": "0px",
                        "boxShadow": "0 0 15px #00ffff, inset 0 0 10px #00ffff",
                        "padding": "15px"
                    },
                    className="mb-3"
                ),
            ], width=12, md=6),
            
            dbc.Col([
                html.Div([
                    html.Label(
                        "RESULT:", 
                        className="mb-2",
                        style={
                            "color": "#ff00ff",
                            "fontWeight": "bold",
                            "textShadow": "0 0 5px #ff00ff",
                            "fontSize": "14px",
                            "letterSpacing": "1px"
                        }
                    ),
                    dbc.Button(
                        "COPY TO CLIPBOARD",
                        id="copy-button",
                        size="sm",
                        className="ms-2 mb-2",
                        style={
                            "backgroundColor": "#ff00ff",
                            "border": "2px solid #ff00ff",
                            "color": "#000000",
                            "fontWeight": "bold",
                            "boxShadow": "0 0 10px #ff00ff",
                            "borderRadius": "0px",
                            "fontFamily": "'Orbitron', monospace",
                            "fontSize": "10px",
                            "letterSpacing": "1px"
                        }
                    ),
                ], style={"display": "flex", "alignItems": "flex-end"}),
                html.Div(
                    id="result-output",
                    children="YOUR SENTIMENT ANALYSIS WILL APPEAR HERE...",
                    style={
                        "minHeight": 200,
                        "padding": "15px",
                        "border": "3px solid #ff00ff",
                        "borderRadius": "0px",
                        "fontSize": 16,
                        "fontFamily": "'Courier New', monospace",
                        "backgroundColor": "#000000",
                        "color": "#00ff00",
                        "boxShadow": "0 0 15px #ff00ff, inset 0 0 10px #ff00ff",
                        "lineHeight": "1.6"
                    },
                    className="mb-3"
                ),
                html.Div(id="result-text", style={"display": "none"}),
                html.Div(
                    id="copy-status", 
                    className="mt-2", 
                    style={
                        "fontSize": 12, 
                        "color": "#00ff00", 
                        "fontWeight": "bold",
                        "textShadow": "0 0 5px #00ff00",
                        "fontFamily": "'Orbitron', monospace"
                    }
                ),
            ], width=12, md=6)
        ]),
        
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id="sentiment-chart",
                    style={"height": 300}
                ),
            ], width=12)
        ], className="mt-3")
    ], fluid=True, className="p-4", style={
        "minHeight": "100vh", 
        "overflowY": "auto",
        "background": "linear-gradient(135deg, #0a0a0a 0%, #1a0033 50%, #000033 100%)",
        "color": "#00ff00"
    })