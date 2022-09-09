#!/usr/bin/python3
"""startin flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def function():
    """display ect"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def function_HBNB():
    """display etc
    """

    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def function_c(text):
    """display etc
    """
    tx = text.replace("_", " ")
    return "C {}".format(tx)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
