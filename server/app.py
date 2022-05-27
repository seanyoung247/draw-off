from flask import Blueprint
from flask import Flask
from timeapp import timeapp

app = Flask(__name__)


# Register apps
timeapp.init(app)


if __name__ == "__main__":
    app.run(debug=True)