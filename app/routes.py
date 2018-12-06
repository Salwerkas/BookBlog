from flask import render_template, flash, redirect, url_for
from app import app
from app.models import User, Book
from app.forms import LoginForm,RegistrationForm
from flask_login import current_user, login_user,logout_user
from flask import request, make_response
from app import db


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title='Home')

@app.route('/show_books', methods=['GET', 'POST'])
def show_books():
	books = Book.query.all()
	return render_template('books.html', title='Books', books=books)

@app.route('/login', methods=['GET','POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		userCookie = request.form['username']
		resp = make_response(render_template('index.html'))
		resp.set_cookie('user', userCookie)
		next_page = request.args.get('next')

		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
			return resp
		return redirect(next_page)
	return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
	logout_user()
	resp = make_response(redirect('/index'))
	resp.delete_cookie('user')
	flash("wylogowano")
	return resp  

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Registered')
		return redirect(url_for('index'))
	return render_template('register.html', title='Register', form=form) 