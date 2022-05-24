import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_time():
    return { "time": time.time() }

if __name__ == "__main__":
    app.run(debug=True)