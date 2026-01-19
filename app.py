"""
Main app module that initializes and configures the Dash application.
"""
from dash import Dash
import dash_bootstrap_components as dbc
from layout import create_layout
from callbacks import register_callbacks


def create_app():
    """
    Create and configure the Dash app instance.
    """
    # Initialize Dash app with Bootstrap theme
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    
    # Set the layout
    app.layout = create_layout()
    
    # Register callbacks
    register_callbacks(app)
    
    return app


# Create the app instance
app = create_app()
