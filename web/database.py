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


def get_user_by_id(user_id):
    """
        Get user by id
    """
    user = find_by_id(user_id)
    if isinstance(user, str):
        return user
    return {
            'id': user.id,
            'username': user.username,
            'email': user.email
            }


def remove(user_id):
    """
        Remove user from DB
    """
    user = find_by_id(user_id)
    if isinstance(user, str):
        return user
    Users.query.filter_by(id=user_id).delete()
    db.session.commit() #pylint: disable=no-member
    return 'Deleted'


def find_by_id(user_id):
    """
        Find user by if user exists
    """
    user = Users.query.filter_by(id=user_id).first()
    if not user:
        return 'User does not exist!'
    return user


def update_user(user_id, username, email):
    """
        Edits username and email in DB
    """
    user = find_by_id(user_id)
    if isinstance(user, str):
        return user
    user.username = username
    user.email = email
    db.session.commit() #pylint: disable=no-member
    return 'Updated'
