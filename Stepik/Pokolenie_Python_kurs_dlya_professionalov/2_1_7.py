
def print_given(*args, **kwargs):
    if args:
        for item in args:
            print(item, type(item))
    if kwargs:
        for key in sorted(kwargs):
            print(key, kwargs[key], type(kwargs[key]))        



print_given(1, [1, 2, 3], 'three', two=2)
print_given('apple', 'cherry', 'watermelon')
print_given(b=2, d=4, c=3, a=1)
print_given()
