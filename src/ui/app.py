"""
Main app module that initializes and configures the Dash application.
"""

import dash_bootstrap_components as dbc
from dash import Dash

from ui.callbacks import register_callbacks
from ui.layout import create_layout


def create_app():
    """
    Create and configure the Dash app instance.
    """
    # Initialize Dash app with Bootstrap theme
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    
    # Add retro custom CSS
    app.index_string = '''
    <!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Orbitron:wght@400;700;900&display=swap');
                * {
                    font-family: 'Orbitron', monospace;
                }
                body {
                    background: linear-gradient(135deg, #0a0a0a 0%, #1a0033 50%, #000033 100%);
                    color: #00ff00;
                }
                h1 {
                    font-family: 'Press Start 2P', cursive;
                    color: #ff00ff;
                    text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 30px #ff00ff;
                    letter-spacing: 2px;
                }
                .retro-glow {
                    box-shadow: 0 0 10px currentColor, 0 0 20px currentColor, inset 0 0 10px currentColor;
                }
            </style>
        </head>
        <body>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
    '''

    # Set the layout
    app.layout = create_layout()

    # Register callbacks
    register_callbacks(app)

    return app


# Create the app instance
app = create_app()
