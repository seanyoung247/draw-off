from flask import Blueprint
from flask import Flask
import time_app.urls


if __name__ == "__main__":
    app = Flask(__name__)

    app.register_blueprint(time_app.urls.bp)

    app.run(debug=True)