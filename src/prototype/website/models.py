#Create DB model

from . import db #import from current folder from __init__
from sqlalchemy.sql import func
from flask_login import UserMixin 
"""Makes it easier to implement user models by providing default 
implementations of the properties and methods required by Flask-Login
 for handling user authentication and session management."""

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    #Associate different information with different user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #class.key_column. Lower letter when do a foreign key for sql


class User(db.Model, UserMixin):
    #Define a schema
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #A list of notes. Reference the name of the class for the relationship

def __repr__(self):
    return f"User('{self.email}', '{self.first_name}')"