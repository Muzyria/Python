n = int(input())
counter = 0
total = 0
mult = 1
last = n % 10
while n != 0:
    a = n % 10
    counter += 1
    total += a
    mult *= a
    n = n // 10
print(total)
print(counter)
print(mult)
print(total/counter)
print(a)
print(last + a)
