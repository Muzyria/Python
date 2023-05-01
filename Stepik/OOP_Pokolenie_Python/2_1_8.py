from functools import wraps
import json


def jsonify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # before
        res = func(*args, **kwargs)
        # after
        return json.dumps(res)

    return wrapper
