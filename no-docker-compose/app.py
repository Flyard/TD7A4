from flask import Flask, render_template
import os
from pymongo import MongoClient

app = Flask(__name__)


@app.route("/")
def index():
    with open("/app/textFile.txt", "r") as f:
        content = f.read() + str(data)
    return render_template("index.html", content = content)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 9000, debug = True)