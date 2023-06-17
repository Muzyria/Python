class Summator:
    m = 1

    def total(self, value):
        return sum(i ** self.m for i in range(1, value + 1))


class SquareSummator(Summator):
    m = 2


class QubeSummator(Summator):
    m = 3


class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m


summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

print(summator1.total(3))    # 1 + 2 + 3
print(summator2.total(3))    # 1 + 4 + 9
print(summator3.total(3))    # 1 + 8 + 27
