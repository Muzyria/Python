import functools

def limiter(limit, unique, lookup):
    def decorator(init_func):
        instances = {}

        @functools.wraps(init_func)
        def wrapper(self, *args, **kwargs):
            value = kwargs.get(unique)
            if value in instances:
                if lookup == 'FIRST':
                    return instances[value][0]
                elif lookup == 'LAST':
                    return instances[value][-1]
            instance = init_func(self, *args, **kwargs)
            if value:
                if value in instances:
                    if len(instances[value]) >= limit:
                        if lookup == 'FIRST':
                            return instances[value][0]
                        elif lookup == 'LAST':
                            return instances[value][-1]
                    else:
                        instances[value].append(instance)
                else:
                    instances[value] = [instance]
            return instance

        return wrapper

    return decorator


class MyClass:
    @limiter(2, 'ID', 'FIRST')
    def __init__(self, ID, value):
        self.ID = ID
        self.value = value

obj1 = MyClass(1, 5)
obj2 = MyClass(2, 8)
obj3 = MyClass(1, 20)
obj4 = MyClass(3, 0)

print(obj3.value)  # 5
print(obj4.value)  # 5
