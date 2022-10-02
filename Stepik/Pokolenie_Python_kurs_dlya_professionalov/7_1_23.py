a = int(input())
b = int(input())
numbers = []

for i in range(a, b + 1):
    if i % 7 == 0:
        numbers.append(i)

print(numbers)
