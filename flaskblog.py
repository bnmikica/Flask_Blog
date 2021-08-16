# enum Module and unique Class were imported automatically as I was typing code for class User
from enum import unique

from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

# This line was imported automatically as I was typing code for atribute posts in class User
from sqlalchemy.orm import backref
from wtforms.validators import Email
from forms import RegistrationForm, LoginForm
import jinja2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eb3f13aa289efe6c7325457574d3307c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# sqlite db simply will be the file on our file system. 
# Class Models are SQL CLasses in SQLAlchemy.
# User Model and Post Model are defined bellow.
# Class Modeles represent Datebase Structure

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # How to specify one to many relation between User and Post Models
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Post('{self.title}', '{self.date_posted}')"

posts = [
    {
        'author': 'Corey Schafer', 
        'title': 'Blog Post 1', 
        'content': 'First post content', 
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe', 
        'title': 'Blog Post 2', 
        'content': 'Second post content', 
        'date_posted': 'April 21, 2018' 
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Accout created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username und password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
