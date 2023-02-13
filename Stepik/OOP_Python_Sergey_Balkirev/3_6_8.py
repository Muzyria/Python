from typing import NoReturn
import sys


class DataBase:


    def __init__(self, path: str) -> NoReturn:
        self.path = path
        self.dict_db = {}

    def write(self, record: 'Record') -> NoReturn:
        self.dict_db[record] = []
        self.dict_db[record].append(record)

    def read(self, pk: int) -> 'Record':
        for k in self.dict_db.values():
            if len(k) == 1 and k[0].pk == pk:
                return k[0]
            else:
                for v in k:
                    if v.pk == pk:
                        return v


class Record:
    PK = 0

    def __init__(self, fio: str, descr: str, old: int) -> NoReturn:
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = self.PK

    def __new__(cls, *args) -> NoReturn:
        cls.PK += 1
        return super().__new__(cls)

    def __hash__(self) -> hash:
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other: 'Record') -> bool:
        return hash(self) == hash(other)


lst_in = list(map(str.strip, sys.stdin.readlines()))
db = DataBase('path')
for i in lst_in:
    text = i.split('; ')
    record = Record(text[0].strip(), text[1].strip(), int(text[2].strip()))
    if record in db.dict_db:
        db.dict_db[record].append(record)
    else:
        db.write(record)
