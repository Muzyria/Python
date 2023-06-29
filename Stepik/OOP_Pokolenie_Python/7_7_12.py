from abc import ABC, abstractmethod

class Stat(ABC):
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self.iterable = iterable

    def add(self, digit):
        self.iterable.append(digit)

    @abstractmethod
    def result(self):
        pass

    def clear(self):
        self.iterable = []

class MinStat(Stat):

    def result(self):
        if self.iterable:
            return min(self.iterable)

class MaxStat(Stat):

    def result(self):
        if self.iterable:
            return max(self.iterable)

class AverageStat(Stat):
    def result(self):
        if self.iterable:
            return sum(self.iterable) / len(self.iterable)


minstat = MinStat([1, 2, 4])
maxstat = MaxStat([1, 2, 4])
averagestat = AverageStat([1, 2, 4])

minstat.add(5)
maxstat.add(5)
averagestat.add(5)

print(minstat.result())
print(maxstat.result())
print(averagestat.result())