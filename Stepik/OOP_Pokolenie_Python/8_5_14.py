def snake_case(attrs=False):
    def decorator(cls):
        class SnakeCaseClass(cls):
            pass

        for name in dir(cls):
            if not name.startswith('__'):
                value = getattr(cls, name)

                if callable(value):
                    snake_case_name = ''.join(['_' + c.lower() if c.isupper() else c for c in name]).lstrip('_')
                    setattr(SnakeCaseClass, name, value)
                elif attrs:
                    setattr(SnakeCaseClass, name, value)

        return SnakeCaseClass

    return decorator


@snake_case()
class MyClass:
    def _FirstMethod(self):
        return 1

    def _superSecondMethod(self):
        return 2


obj = MyClass()

print(obj._first_method())
print(obj._super_second_method())