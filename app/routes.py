from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title='Home')

@app.route('/show_books', methods=['GET', 'POST'])
def show_books():
    return render_template('books.html', title='Books')

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)