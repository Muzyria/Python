class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __get_name(self):
        return self.__name


    def __get_salary(self):
        return self.__salary


    def __set_salary(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self.__salary = value
        else:
            print(f"ErrorValue:{value}")

    # title = property(fget=__get_name)
    # reward = property(fget=__get_salary, fset=__set_salary)

    @property
    def title(self):
        return self.__get_name()

    @property
    def reward(self):
        return self.__get_salary()

    @reward.setter
    def reward(self, value):
        self.__set_salary(value)

# Напишите определение класса Employee


# Ниже код для проверки методов класса Employee
employee = Employee("John Doe", 50000)
assert employee.title == "John Doe"
assert employee._Employee__name == "John Doe"
assert isinstance(employee, Employee)
assert isinstance(type(employee).title, property), 'Вы не создали property title'
assert isinstance(type(employee).reward, property), 'Вы не создали property reward'

assert employee.reward == 50000
employee.reward = -100  # ErrorValue:-100

employee.reward = 1.5
assert employee.reward == 1.5

employee.reward = 70000
assert employee.reward == 70000
employee.reward = 'hello'  # Печатает ErrorValue:hello
employee.reward = '777'  # Печатает ErrorValue:777
employee.reward = [1, 2]  # Печатает ErrorValue:[1, 2]
assert employee.reward == 70000
employee._Employee__set_salary(55000)
assert employee._Employee__get_salary() == 55000
