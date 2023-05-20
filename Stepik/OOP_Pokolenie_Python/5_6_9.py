class Calculator:
    def __call__(self, a, b, operation):
        match operation:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                if b != 0:
                    return a / b
                return "Деление на ноль невозможно"


calculator = Calculator()

print(calculator(10, 5, '+'))
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*'))
print(calculator(10, 5, '/'))