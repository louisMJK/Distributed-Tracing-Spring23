from random import randint
from flask import Flask
from opentelemetry import trace, metrics


# Acquire tracer & meter
tracer = trace.get_tracer(__name__)
meter = metrics.get_meter(__name__)

# create a counter instrument to make measurements with
roll_counter = meter.create_counter(
    "roll_counter", 
    description="Number of rolls by roll value"
)

app = Flask(__name__)

@app.route("/")
def roll_dice():
    s = "Roll dice result: " + str(do_roll()) + "\n"
    return s

def do_roll():
    # creates a new span that's the child of the current one
    with tracer.start_as_current_span("do_roll") as rollspan:
        res = randint(1, 6)
        rollspan.set_attribute("roll.value", res)
        roll_counter.add(1, {"roll.value": res})
        return res

