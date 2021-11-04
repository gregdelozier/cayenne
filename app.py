
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_index():
    return 'Hello from the second version of the Cayenne app!'

@app.route('/bye')
def get_bye():
    return 'Goodbye from Cayenne!!!'


