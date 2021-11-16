
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def get_index():
    return 'Hello from the really extremely great second version of the Cayenne app!'

@app.route('/bye')
def get_bye():
    return 'Goodbye from cayenne!!!'


