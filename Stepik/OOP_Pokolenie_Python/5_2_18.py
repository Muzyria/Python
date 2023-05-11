class AnyClass:
    def __init__(self, **kwargs):
        [setattr(self, key, value) for key, value in kwargs.items()]

    def __repr__(self):
        return f"{self.__class__.__name__}('{x}')"

    def __str__(self):
        return f"{self.__class__.__name__}: {x}"


