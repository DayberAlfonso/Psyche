from textblob import TextBlob
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"


# Initialize Dash app with Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout
app.layout = dbc.Container([
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
            dbc.Button(
                "Analyze Sentiment",
                id="analyze-button",
                color="primary",
                className="mb-3",
                n_clicks=0
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

# Callback to analyze sentiment when button is clicked
@app.callback(
    Output("result-output", "children"),
    Input("analyze-button", "n_clicks"),
    State("text-input", "value"),
    prevent_initial_call=True
)
def update_sentiment(n_clicks, text):
    if not text or text.strip() == "":
        return html.Div(
            "Please enter some text to analyze.",
            style={"color": "#6c757d"}
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
    
    return html.Div([
        html.H4(f"Sentiment: {sentiment} {emoji}", style={"color": color, "marginBottom": "10px"}),
        html.P(f"You entered: \"{text}\"", style={"color": "#6c757d", "fontSize": 14})
    ])


if __name__ == "__main__":
    app.run(debug=True)