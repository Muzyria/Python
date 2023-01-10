class SingletonFive:
    __instans = None
    __count = 0
    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__instans = super().__new__(cls)
            cls.__count += 1

        return cls.__instans    

    def __init__(self, name):
        self.name = name

"""
class SingletonFive:
    __instances = []
    def __new__(cls, *args, **kwargs):
        if len(cls.__instances) < 5:
            cls.__instances.append(super().__new__(cls))
        return cls.__instances[-1]
    def __init__(self, name):
        self.name = name
objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять
"""

            


