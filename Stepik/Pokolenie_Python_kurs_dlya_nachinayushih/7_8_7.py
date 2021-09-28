# put your python code here
n = int(input())
for j in range(1, n + 1):
    for i in range(1, 10):
        print(j, '+', i, '=', j + i, end='\n')
    print()