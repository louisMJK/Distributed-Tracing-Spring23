from random import randint
from flask import Flask


app = Flask(__name__)

@app.route("/")
def roll_dice():
    s = "Roll dice result: " + str(do_roll()) + "\n"
    return s

def do_roll():
    res = randint(1, 6)
    return res

