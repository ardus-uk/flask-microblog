from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Admin'}
    posts = [
        {
            'author': {'username': 'Peter'},
            'body': 'Beautiful day in Ireby!'
        },
        {
            'author': {'username': 'Ruth'},
            'body': 'The waters of Bassenthwaite are refreshing!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        f_username = form.username.data
        f_remember_me = form.remember_me.data
        flash('Login requested for user {}, remember_me={}'.format(f_username, f_remember_me))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
