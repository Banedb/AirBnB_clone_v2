#!/usr/bin/python3
"""100-hbnb module"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def cleanup(exception):
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays an html template."""
    return render_template("100-hbnb.html",
                           states=storage.all(State),
                           amenities=storage.all(Amenity),
                           places=storage.all(Place))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
