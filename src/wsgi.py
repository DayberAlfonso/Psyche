"""
WSGI entry point for gunicorn.
This file exposes the Flask WSGI application from the Dash app.
"""
from ui.app import app

# Gunicorn expects a variable named 'application' by default
# Dash apps expose their Flask server via the .server attribute
application = app.server
