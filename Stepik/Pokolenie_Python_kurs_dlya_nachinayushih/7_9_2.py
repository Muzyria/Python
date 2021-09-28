n = int(input())

for j in range(1, n + 1):
    for i in range(1, j + 1):
        print(i, end='')
    for q in range(j -1, 0, -1):
        print(q, end='') 
    print()