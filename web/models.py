"""
    Using for DB tables
"""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model): #pylint: disable=too-few-public-methods
    """
        Discribes User table in DB
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) #pylint: disable=no-member
    username = db.Column(db.String(80)) #pylint: disable=no-member
    email = db.Column(db.String(80), unique=True) #pylint: disable=no-member

    def __init__(self, user_id, username, email):
        self.id = user_id #pylint: disable=invalid-name
        self.username = username
        self.email = email
