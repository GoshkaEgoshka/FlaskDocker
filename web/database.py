"""
    This module discribes work with DB.
    There are add, delete, get, update methods.
"""
from .models import db, Users


async def add_user_to_db(**kwargs):
    """
        Add user to DB
    """
    user = Users(**kwargs)
    db.session.add(user) #pylint: disable=no-member
    db.session.commit() #pylint: disable=no-member


async def get_users():
    """
        Get all users from DB
    """
    users = Users.query.all()
    all_users = [
        {
            'id': user.id,
            'username': user.username,
            'email': user.email
        } for user in users
    ]
    return all_users


def find_user_by_id(func):
    """
        Decorator checks if user exists in DB
    """
    async def wrapper(**kwargs):
        query = Users.query.filter_by(
            id=kwargs['id']
        )
        user = query.first()
        if not user:
            return 'User does not exist!'
        return await func(query, **kwargs)
    return wrapper


@find_user_by_id
async def get_user_by_id(query, **kwargs):
    """
        Get user by id
    """
    user = query.first()
    return {
    'id': user.id,
    'username': user.username,
    'email': user.email
    }

@find_user_by_id
async def remove_user(query, **kwargs):
    """
        Remove user from DB
    """
    query.delete()
    db.session.commit() #pylint: disable=no-member
    return 'Deleted'


@find_user_by_id
async def update_user(query, **kwargs):
    """
        Edits username and email in DB
    """
    kwargs.pop('id', None)
    query.update(kwargs)
    db.session.commit() #pylint: disable=no-member
    return 'Updated'
