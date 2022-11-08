#!/usr/bin/python3
""" A script thats starts a Flask web application."""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/airbnb-onepage/')
def hello_hbnb():
    """ a function that returns the string 'Hello HBNB!'."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
