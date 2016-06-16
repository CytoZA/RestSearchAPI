from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World! Coming from inside a container on a VM."


if __name__ == "__main__":
    app.run()
