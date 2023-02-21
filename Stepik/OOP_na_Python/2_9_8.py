class RobotVacuumCleaner:
    name = 'Henry'
    charge = 25

    @classmethod
    def update_charge(cls, new_value):
        cls.charge = new_value

    @staticmethod
    def hello(name):
        return f'Привет, {name}'

    @property
    def data(self):
        return {
            'name': self.name,
            'charge': self.charge
        }


    def make_clean(self):
        if self.charge < 30:
            return 'Кожаный, заряди меня! Я слаб'
        return 'Я вычищу твою берлогу!!!'

# код ниже не нужно удалять, в нем находятся проверки
print(RobotVacuumCleaner.hello('Господин'))
RobotVacuumCleaner.update_charge(50)

robot = RobotVacuumCleaner()
print(robot.make_clean())
print(robot.data)

RobotVacuumCleaner.update_charge(False)
print(robot.make_clean())
