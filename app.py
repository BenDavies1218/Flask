from flask import Flask
import json
import random

app = Flask("abc")

@app.route("/coinflip")

def coinflip():
    outcomes = {"result": "Heads", "result": "Tails"}
    result = random.sample(outcomes, 1)
    return json.dumps(result, indent=4, separators=('. ', ' = '))