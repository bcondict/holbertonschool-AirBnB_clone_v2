#!/usr/bin/python3
""" starts a Flask web application"""


from re import A
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_HBNB():
    """display 'Hello HBNB!' """
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    """display HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def c_plus_text(text):
    """ display “C ” followed by the value of the text """
    my_text = text.replace("_", " ")
    return "C {}".format(my_text)


@app.route("/python", defaults={'text': "is cool"})
@app.route("/python/<text>")
def python_text(text):
    """ display “Python ”, followed by the value of the text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def num(n):
    """ dipslay n is a number only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """ display a HTML page only if n is an integer"""
    return render_template('5-number.html', num=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """display a HTML page only if n is an integer and if is odd or even"""
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
