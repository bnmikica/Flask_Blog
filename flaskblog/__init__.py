# enum Module and unique Class were imported automatically as I was typing code for class User
from enum import unique

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# This line was imported automatically as I was typing code for atribute posts in class User
from sqlalchemy.orm import backref
from wtforms.validators import Email
# This line is copied/pasted into routes.py file
# from forms import RegistrationForm, LoginForm
import jinja2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eb3f13aa289efe6c7325457574d3307c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
