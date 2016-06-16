from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World! Coming from " + os.environ['OS'] + ". <br> This is a test. "


if __name__ == "__main__":
    app.run()
