from collections import UserDict

class BirthdayDict(UserDict):
    def __setitem__(self, key, value):
        if value in self.data.values():
            print(f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
        self.data.__setitem__(key, value)


from datetime import date

birthdaydict = BirthdayDict()

birthdaydict['Боб'] = date(1987, 6, 15)
birthdaydict['Том'] = date(1984, 7, 15)
birthdaydict['Мария'] = date(1987, 6, 15)
