from flask import session, redirect, url_for
from functools import wraps

def login_check(func):
    @wraps(func)
    async def decorated_function(*args, **kwargs):
        if not session.get('login', False):
            return redirect(url_for('get_authorization'))
        return await func(*args, **kwargs)
    return decorated_function
   