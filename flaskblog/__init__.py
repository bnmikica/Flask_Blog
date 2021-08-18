# enum Module and unique Class were imported automatically as I was typing code for class User
from enum import unique

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Flask extensions like flask_bcrypt, flask_login
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager

# This line was imported automatically as I was typing code for atribute posts in class User
from sqlalchemy.orm import backref
from wtforms.validators import Email
# from wtforms.validators import DataRequired, Length, Email, EqualTo
# This line is copied/pasted into routes.py file
# from forms import RegistrationForm, LoginForm
import jinja2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eb3f13aa289efe6c7325457574d3307c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from flaskblog import routes
