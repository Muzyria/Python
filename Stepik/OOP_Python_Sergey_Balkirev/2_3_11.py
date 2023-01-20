class TVProgram:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    def add_telecast(self, tl: object):
        self.items.append(tl)

    def remove_telecast(self, indx: int):
        self.items = [item for item in self.items if item.uid != indx]


class Telecast:
    def __init__(self, id: int, name: str, duration: int):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value: int):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value: int):
        self.__duration = value


if __name__ == '__main__':
    pr = TVProgram("Первый канал")
    pr.add_telecast(Telecast(1, "Доброе утро", 10000))
    pr.add_telecast(Telecast(2, "Новости", 2000))
    pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
    pr.remove_telecast(1)
    for t in pr.items:
        print(f"{t.name}: {t.duration}")