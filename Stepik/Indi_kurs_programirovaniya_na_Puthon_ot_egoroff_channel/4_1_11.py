n = int(input())
floor = 1
count = 1
b = 0
while b < n:
    floor += 1
    count += floor
    b += count
print(floor -1)