# import json
#
# def jsonify(func):
#     def inner(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return json.dumps(result)
#
#     return inner
#
#
#
# @jsonify
# def make_user(id, live, options):
#     return {'id': id, 'live': live, 'options': options}
#
#
# print(make_user(4, False, None))

def repeater(func):
    def inner(*args):
        func(*args)
        func(*args)
    return inner

@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 7) # после этого на отдельных строка дважды распечатается значение 14
multiply(5, 3) # после этого на отдельных строка дважды распечатается значение 15