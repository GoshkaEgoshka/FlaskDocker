"""
    This module discribes work with DB.
    There are add, delete, get, update methods.
"""
from models import db, Users


def add_user_to_db(**kwargs):
    """
        Add user to DB
    """
    user = Users(**kwargs)
    db.session.add(user) #pylint: disable=no-member
    db.session.commit() #pylint: disable=no-member


def get_users():
    """
        Get all users from DB
    """
    users = Users.query.all()
    all_users = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return all_users


def find_by_id(func):
    """
        Decorator checks if user exists in DB
    """
    def wrapper(user_id):
        user = Users.query.filter_by(id=user_id).first()
        if not user:
            return 'User does not exist!'
        return func(user_id)
    return wrapper


@find_by_id
def get_user_by_id(user_id):
    """
        Get user by id
    """
    user = Users.query.filter_by(id=user_id).first()
    return {
            'id': user.id,
            'username': user.username,
            'email': user.email
            }


@find_by_id
def remove(user_id):
    """
        Remove user from DB
    """
    Users.query.filter_by(id=user_id).delete()
    db.session.commit() #pylint: disable=no-member
    return 'Deleted'


def update_user(**kwargs):
    """
        Edits username and email in DB
    """
    Users.query.filter_by(id=kwargs[0]).update(**kwargs)
    db.session.commit() #pylint: disable=no-member
    return 'Updated'
