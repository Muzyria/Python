class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self.matrix = [[self.value] * self.cols for _ in range(self.rows)]

    def get_value(self, row, col):
        return self.matrix[row][col]

    def set_value(self, row, col, value):
        self.matrix[row][col] = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.rows}, {self.cols})"

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.matrix)

    def __pos__(self):
        return Matrix(self.rows, self.cols, self.value)

    def __neg__(self):
        return Matrix(self.rows, self.cols, -self.value)

    def __invert__(self):
        res = Matrix(self.cols, self.rows)
        for i in range(self.cols):
            for j in range(self.rows):
                res.set_value(i, j, self.matrix[j][i])
        return res

    def __round__(self, n=None):
        if n is None:
            return Matrix(self.rows, self.cols, round(self.value))
        return Matrix(self.rows, self.cols, round(self.value, n))






    # def __pos__(self):
    #     result = Matrix(len(self.matrix), len(self.matrix[0]))
    #     for i in range(self.rows):
    #         for j in range(self.cols):
    #             result.set_value(i, j, self.matrix[i][j])
    #     return result
    #
    # def __neg__(self):
    #     result = Matrix(len(self.matrix), len(self.matrix[0]))
    #     for i in range(self.rows):
    #         for j in range(self.cols):
    #             result.set_value(i, j, -self.matrix[i][j])
    #     return result
    #
    # def __invert__(self):
    #     result = Matrix(len(self.matrix[0]), len(self.matrix))
    #     for i in range(self.cols):
    #         for j in range(self.rows):
    #             result.set_value(i, j, self.matrix[j][i])
    #     return result
    #
    # def __round__(self, n=None):
    #     result = Matrix(len(self.matrix), len(self.matrix[0]))
    #     for i in range(self.rows):
    #         for j in range(self.cols):
    #             result.set_value(i, j, round(self.matrix[i][j], n))
    #     return result

matrix = Matrix(4, 2)

counter = 1
for row in range(4):
    for col in range(2):
        matrix.set_value(row, col, counter)
        counter += 1

print(matrix)
print()
print(~matrix)