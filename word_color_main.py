"""
This is the driver module
"""

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
import wordcolor.image_processor as ip


@app.route('/')
def index(name=None):
    return render_template('hello.html', name=name)


@app.route('/color')
def color():
    phrase = request.args.get('word')
    common_color = ip.download_image_and_extract_color(phrase)
    data = {'phrase': phrase, 'color': common_color}
    return render_template('color.html', data=data)
