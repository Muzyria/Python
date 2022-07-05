class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.money = 0

    def can_add(self, v):
        return True if (self.capacity - self.money) >= v else False

    def add(self, v):
        if self.can_add(v):
            self.money += v
