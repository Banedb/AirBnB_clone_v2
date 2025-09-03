#!/usr/bin/python3
"""10-hbnb_filters module"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def cleanup(exception):
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def home():
    """Displays an html template."""
    states = storage.all(State)
    am = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states, amenities=am)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
