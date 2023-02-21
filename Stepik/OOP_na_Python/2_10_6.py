class Robot:
    population = 0

    def __init__(self, name):
        self.nane = name
        print(f"Робот {self.nane} был создан")
        Robot.population += 1

