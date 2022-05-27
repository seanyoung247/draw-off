"""
Main file for this app
"""

from . import urls
from flask import Blueprint


def init(app):
    """ Initiates this app and attaches it to the flask instance passed. """

    # Create this apps blueprint
    bp = Blueprint(
        name="timeapp",
        import_name="timeapp",
    )

    # Import the defined routes
    urls.add_urls(bp)

    # Attach it to the flask instance
    app.register_blueprint(bp)

