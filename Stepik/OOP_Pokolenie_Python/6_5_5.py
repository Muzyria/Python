class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value:
            pass
        return True


print('start')

with SuppressAll():
    print('Python generation!')
    raise ValueError

print('end')


print('start')

with SuppressAll():
    print('Python generation!')

print('end')
