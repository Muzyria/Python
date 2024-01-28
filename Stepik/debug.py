

class Matrix:
    def __init__(self, rows: int, cols: int, value: int = 0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[value] * cols for _ in range(rows)]

    def get_value(self, row: int, col: int):
        pass

    def set_value(self, row: int, col: int, value: int):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}({self.rows}, {self.cols})"

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.matrix)


print(Matrix(2, 3))
