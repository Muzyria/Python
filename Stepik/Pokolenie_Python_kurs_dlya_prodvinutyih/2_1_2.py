# put your python code here
def count(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a % b)
    print((a ** 10 + b ** 10) ** 0.5)

a, b = int(input()), int(input())
count(a, b)