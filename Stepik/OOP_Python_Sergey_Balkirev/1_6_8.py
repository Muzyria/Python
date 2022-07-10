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

            


