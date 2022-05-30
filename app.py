from flask import Flask
from timeapp import timeapp
from reactapp import reactapp

app = Flask(__name__, static_folder=None)


# Register apps
timeapp.init(app)
reactapp.init(app, 'frontend')


if __name__ == "__main__":
    app.run(debug=True)