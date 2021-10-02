n = int(input())
count3 = 0
countLast = 0
countChet = 0
sumBig5 = 0
multyBig7 = 1
count05 = 0
last = n % 10
while n > 0:
    x = n % 10
    if x == 3:
        count3 += 1
    if x == last:
        countLast += 1
    if x % 2 == 0:
        countChet += 1
    if x > 5:
        sumBig5 += x
    if x > 7:
        multyBig7 *= x
    if x == 0 or x == 5:
        count05 += 1
    n //= 10
print(count3)
print(countLast)
print(countChet)
print(sumBig5)
print(multyBig7)
print(count05)