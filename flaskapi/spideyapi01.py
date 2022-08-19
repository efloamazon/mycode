#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

app= Flask(__name__)

herodata= [{
    "name": "Spiderman",
    "realName": "Peter Parker",
    "since": 1962,
    "powers": [
        "Wall crawling",
        "web shooters",
        "spder senses"
        ]
        }]
@app.route("/")
def index():
    return jsonify(herodata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
