#!/usr/bin/python3
"""6-number_odd_or_even module"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Displays `Hello HBNB!`."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays `HBNB`."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def print_c(text):
    """Displays C followed by text passed in."""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def print_python(text):
    """Displays Python followed by text passed in."""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def check_num(n):
    """Checks if a number was passed in."""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    """Renders an html template if a valid number was passed in."""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """Renders html stating parity of number if a number was passed in."""
    parity = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, parity=parity)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
