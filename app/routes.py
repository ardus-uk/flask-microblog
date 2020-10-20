from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Peter'}
    return render_template('index.html', title='Home', user=user)  

@app.route('/hello')

def hello():
    user = {'username': 'Ruth'}
    return render_template('hello.html', title='Home', user=user)  