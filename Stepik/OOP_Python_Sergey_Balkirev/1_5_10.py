import sys


class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None


    def link(self, obj):
        self.next_obj = obj


lst_in = ['1. Первые шаги в ООП',
          '1.1 Как правильно проходить этот курс',
          '1.2 Концепция ООП простыми словами',
          '1.3 Классы и объекты. Атрибуты классов и объектов',
          '1.4 Методы классов. Параметр self',
          '1.5 Инициализатор init и финализатор del',
          '1.6 Магический метод new. Пример паттерна Singleton',
          '1.7 Методы класса (classmethod) и статические методы (staticmethod)']


head_obj = ListObject(lst_in[0])
obj = head_obj

for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)
    obj = obj_new



a = [1, 2, 3]
list.append(a, 5)
list.append(a, 9)
print(a) # [1, 2, 3, 5]