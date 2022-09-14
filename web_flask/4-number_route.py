#!/usr/bin/python3
""" starts a Flask web application"""


from email.policy import default
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
