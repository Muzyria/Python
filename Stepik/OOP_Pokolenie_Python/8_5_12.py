import json

def jsonattr(filename):
    def decorator(cls):
        with open(filename, 'r') as file:
            data = json.load(file)
            for key, value in data.items():
                setattr(cls, key, value)
        return cls
    return decorator
