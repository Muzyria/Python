class Person:
    def __init__(self, name, passport):
        self.name = name
        self.passport = passport
        

    def display(self):
        print(f"{self.name}: {self.passport}")


class Employee(Person):
    def __init__(self, name, passport, salary, department):
        super().__init__(name, passport)
        self.salary = salary
        self.department = department



a = Employee('Raul', 886012, 200000, "QA")
a.display() # печатает "Raul: 886012"       