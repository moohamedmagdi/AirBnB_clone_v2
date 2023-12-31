#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """function to return Hello HBNB!"""
    return render_template("10-hbnb_filter.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=None)
