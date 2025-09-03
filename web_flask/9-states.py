#!/usr/bin/python3
"""9-states module"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def cleanup(exception):
    storage.close()


@app.route("/states", strict_slashes=False)
def list_states():
    """Lists all State objects, sorted by name."""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def list_state(id):
    """Lists all City objects in a State object, sorted by name."""
    states = storage.all(State)
    state = states.get(f"State.{id}", None)
    return render_template("9-states.html", state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
