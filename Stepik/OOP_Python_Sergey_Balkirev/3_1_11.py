import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def __setattr__(self, key, value):
        if key == 'slot_1' and not (value is None or isinstance(value, Mechanical)):
            return
        if key == 'slot_2' and not (value is None or isinstance(value, Aragon)):
            return
        if key == 'slot_3' and not (value is None or isinstance(value, Calcium)):
            return
        super().__setattr__(key, value)

    def add_filter(self, slot_num: int, my_filter: object):
        if slot_num == 1 and self.slot_1 is None:
            self.slot_1 = my_filter
        if slot_num == 2 and self.slot_2 is None:
            self.slot_2 = my_filter
        if slot_num == 3 and self.slot_3 is None:
            self.slot_3 = my_filter

    def remove_filter(self, slot_num):
        if slot_num == 1:
            self.slot_1 = None
        if slot_num == 2:
            self.slot_2 = None
        if slot_num == 3:
            self.slot_3 = None

    def get_filters(self):
        return self.slot_1, self.slot_2, self.slot_3

    def water_on(self):
        return all(self.get_filters()) and all(
            [0 <= (time.time() - fltr.date) <= self.MAX_DATE_FILTER for fltr in self.get_filters()])


class Mechanical:
    def __init__(self, date: float):
        self.__date = date

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
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
