from . import urls
from flask import Blueprint


def init(app):
    bp = Blueprint(
        name="time_app",
        import_name="time_app",
    )
    urls.add_urls(bp)
    app.register_blueprint(bp)

