

class Calculator:
    def divide(self, x: int | float, y: int | float) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("TYPE ERROR")
        if y == 0:
            raise ZeroDivisionError("ZERO_DIVISION)ERROR")
        return x / y

    def add(self, x: int | float, y: int | float) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("TYPE ERROR")
        return x + y


if __name__ == "__main__":
    pass
