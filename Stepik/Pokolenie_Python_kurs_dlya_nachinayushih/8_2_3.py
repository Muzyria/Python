n = 4
count = 0
maximum = -10**8
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
            #break
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')