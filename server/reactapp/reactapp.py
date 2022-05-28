"""
Main reactapp module.

Performs Setup and attaches to flask app.
"""

from . import urls
from flask import Blueprint

def init(app):
    """
    Initiates this app and attaches it to the flask instance passed.
    """
    bp = Blueprint( 
        name="reactapp", import_name='reactapp', 
        template_folder='./templates'
    )

    urls.add_urls(bp)

    app.register_blueprint(bp)