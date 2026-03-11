from functools import wraps
from flask import session, jsonify

def role_required(roles):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            if "role" not in session:
                return jsonify({"message": "Login required"}), 401

            if session["role"] not in roles:
                return jsonify({"message": "Access denied"}), 403

            return func(*args, **kwargs)

        return wrapper

    return decorator