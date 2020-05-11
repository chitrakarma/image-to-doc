from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/login')
def login():
    return render_template('index.html.jinja', name="Index")


@app.route('/register')
def register():
    return "Welcome to the register page"
