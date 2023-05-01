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

# import json
#
# def jsonify(func):
#     def wrapper(*args):
#         wrapper.__name__ = func.__name__
#         wrapper.__doc__ = func.__doc__
#         return json.dumps(func(*args))
#     return wrapper
