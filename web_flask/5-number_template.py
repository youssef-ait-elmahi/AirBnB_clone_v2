#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_text(text='is cool'):

    """
    This function takes a string argument 'text',
    replaces all underscores with spaces,
    and returns a string in the format 'Python <text>'
    when the /python/<text> route is accessed.
    Args:
        text (str): The text to be displayed after 'Python '
    Returns:
        str: A string in the format 'Python <text>'
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    This function takes an integer argument 'n'
     and returns a string in the format '<n> is a number'
    when the /number/<n> route is accessed.
    Args:
        n (int): The number to be displayed
    Returns:
        str: A string in the format '<n> is a number'
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """return render_template('number.html', n=n)"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
