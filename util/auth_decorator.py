from flask import redirect, session, url_for
from functools import wraps

def authorization():
    def _authorization(f):
        @wraps(f)
        def __authorization(*args, **kwargs):
            if 'user' not in session:
                result = redirect(url_for('routes.login'))
            elif 'user' in session:
                result = f(*args, **kwargs)
            return result
        return __authorization
    return _authorization