
class Clock:
    def __init__(self, tm):
        self.__time = 0
        if self.__check_time(tm):
            self.__time = tm

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @classmethod
    def __check_time(cls, tm):
        return type(tm) == int and 0 <= tm <= 100000


clock = Clock(-4530)
print(clock.get_time())  # 4530

clock = Clock(4530)
clock.set_time(15)
print(clock.get_time())  # 15
clock.set_time(7)
clock.set_time(-1)
clock.set_time('2')
clock.set_time(0.1)
print(clock.get_time())  # 7


"""
class Clock:
    def __init__(self, tm):
        self.__time = 0
        self.set_time(tm)

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @classmethod
    def __check_time(cls, tm):
        if type(tm) == int and 0 <= tm <= 100000:
            return True
        return False

"""
