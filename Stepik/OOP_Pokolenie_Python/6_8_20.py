class Versioned:
    def __init__(self):
        self._history = {}

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if obj not in self._history:
            raise AttributeError('Атрибут не найден')
        version = self._history[obj][0]
        values = self._history[obj][1]
        return values[version]

    def __set__(self, obj, value):
        values = self._history.setdefault(obj, [-1, []])[1]
        values.append(value)

    def get_version(self, obj, n):
        values = self._history[obj][1]
        return values[n - 1]

    def set_version(self, obj, n):
        self._history[obj][0] = n - 1



class Student:
    age = Versioned()

student1 = Student()
student2 = Student()

student1.age = 18
student1.age = 19
student1.age = 20

student2.age = 30
student2.age = 31
student2.age = 32

print(student1.age)
print(student2.age)
Student.age.set_version(student1, 1)
Student.age.set_version(student2, 1)
print(student1.age)
print(student2.age)

