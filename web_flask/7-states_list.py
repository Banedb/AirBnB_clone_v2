#!/usr/bin/python3
"""7-states_list module"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def cleanup(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    """Lists all State objects present in DBStorage sorted by name."""
    states = storage.all(State).values()
    states = sorted(states, key=lambda s: s.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
