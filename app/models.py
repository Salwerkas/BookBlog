from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from app import db
from flask_login import LoginManager
from app import admin

from flask_admin.contrib.sqla import ModelView



class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(40), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	
	def set_password(self,password):
		self.password_hash = generate_password_hash(password)


	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User {}>'.format(self.username)

class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(255), index=True)
	description = db.Column(db.String(255))
	author = db.Column(db.String(255))
	pages = db.Column(db.Integer)


class Opinion(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

	def __repr__(self):
		return '<Post {}'.format(self.body)

admin.add_view(ModelView(Book, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Opinion, db.session))



@login.user_loader
def load_user(id):
	return User.query.get(int(id))

