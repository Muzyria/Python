class Scales:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, n):
        self.right += n

    def add_left(self, n):
        self.left += n

    def get_result(self):
        if self.left < self.right:
            return 'Правая чаша тяжелее'
        if self.left > self.right:
            return 'Левая чаша тяжелее'
        return 'Весы в равновесии'
