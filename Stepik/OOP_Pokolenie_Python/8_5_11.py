def add_attr_to_class(**attrs):
    def decorator(cls):
        for attr, value in attrs.items():
            setattr(cls, attr, value)
        return cls
    return decorator
