from flask import Flask, Blueprint, send_from_directory
from timeapp import timeapp
from reactapp import reactapp

app = Flask(__name__, static_folder=None)


# Register apps
timeapp.init(app)
reactapp.init(app)


if __name__ == "__main__":
    app.run(debug=True)