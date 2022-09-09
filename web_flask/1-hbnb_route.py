#!/usr/bin/python3
"""Starting flask
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def function():
    """Displating etc
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def function_HBNB():
    """Displaying etc
    """

    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
