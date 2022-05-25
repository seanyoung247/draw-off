from flask import Blueprint
from flask import Flask
from time_app.blueprint import time_bp
import time_app.urls

# @app.route('/time')
# def get_time():
#     return { "time": time.time() }

if __name__ == "__main__":
    app = Flask(__name__)

    app.register_blueprint(time_bp)

    app.run(debug=True)