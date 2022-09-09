#!/usr/bin/python3
"""starting flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def function():
    """display etc"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def function_HBNB():
    """display ect"""

    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def function_c(text):
    """dislay ect"""
    tx = text.replace("_", " ")
    return "C {}".format(tx)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def function_python(text="is cool"):
    """display ect"""
    tx = text.replace("_", " ")
    return "Python {}".format(tx)


@app.route("/number/<int:n>", strict_slashes=False)
def function_number(n):
    """display ect"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
