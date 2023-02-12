
class IterColumn:
    def __init__(self, lst: list, column: int):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for i in range(len(self.lst)):
            yield self.lst[i][self.column]
