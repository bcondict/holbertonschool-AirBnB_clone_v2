#!/usr/bin/python3
""" starts a Flask web application"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_close(self):
    """cleases sqlalchemy session"""
    storage.close()


@app.route('/states_list')
def states_list():
    """display html page"""
    my_dict = storage.all(State)
    return render_template('7-states_list.html', state_dict=my_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
