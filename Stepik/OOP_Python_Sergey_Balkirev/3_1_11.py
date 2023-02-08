import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def add_filter(self, slot_num, filter):
        if slot_num == 1 and self.slot_1 is None:
            self.slot_1 = filter
        if slot_num == 2 and self.slot_2 is None:
            self.slot_2 = filter
        if slot_num == 3 and self.slot_3 is None:
            self.slot_3 = filter



class Mechanical:
    def __init__(self, date: float):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        print("__setter")
        pass

class Aragon:
    def __init__(self, date: float):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        pass


class Calcium:
    def __init__(self, date: float):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        pass
