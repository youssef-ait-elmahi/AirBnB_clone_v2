#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ Method that returns Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Method that returns HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    This function takes a string argument 'text',
    replaces all underscores with spaces,
    and returns a string in the format 'C <text>'
    when the /c/<text> route is accessed.
    Args:
        text (str): The text to be displayed after 'C '
    Returns:
        str: A string in the format 'C <text>'
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
