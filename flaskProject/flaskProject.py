# all the imports
from flask import Flask, render_template

app= Flask(__name__)


@app.route('/')
def home():
    """
    Render a Hello World response.

    :return: Flask response
    """
    return 'Hello World!'
