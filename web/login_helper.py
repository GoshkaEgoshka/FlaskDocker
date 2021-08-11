"""
    Helper for login
"""
from functools import wraps
from flask import session, redirect, url_for


def login_check(func):
    """
        Check login decorator
    """
    @wraps(func)
    async def decorated_function(*args, **kwargs):
        if not session.get('login', False):
            return redirect(url_for('get_authorization'))
        return await func(*args, **kwargs)
    return decorated_function
