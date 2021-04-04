"""
This is the driver module
"""

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
import wordcolor.image_processor as ip
import DuckDuckGoImages as ddg
import os


@app.route('/')
def index(name=None):
    return render_template('hello.html', name=name)


@app.route('/color')
def color():
    phrase = request.args.get('word')
    # check if this phrase already exists
    path = 'images/' + phrase
    if os.path.isdir(path):
        if len(os.listdir(path)) > 0:
            print('Image directory already exists for the phrase: ' + phrase)
    else:
        print("Downloading images...\n\n")
        ddg.download(phrase, "images/" + phrase, 5)
    common_color = ip.get_common_color_v3("images/" + phrase)
    data = {'phrase': phrase, 'color': common_color}
    return render_template('color.html', data=data)
