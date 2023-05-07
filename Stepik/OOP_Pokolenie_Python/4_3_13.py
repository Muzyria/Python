class Todo:
    def __init__(self):
        self.things = []

    def add(self, case, priority):
        self.things.append((case, priority))

    def get_by_priority(self, priority):
        return [item[0] for item in self.things if item[1] == priority]

    def get_low_priority(self):
        return [item[0] for item in self.things if item[1] == sorted(self.things, key=lambda x: x[1])[0][1]]

    def get_high_priority(self):
        return [item[0] for item in self.things if item[1] == sorted(self.things, key=lambda x: x[1])[-1][1]]
