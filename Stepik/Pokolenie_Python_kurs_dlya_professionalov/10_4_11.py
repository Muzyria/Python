class PowerOf:
    def __init__(self, number):
        self.number = number
        self.step = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.step += 1
        return self.number ** self.step


power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
