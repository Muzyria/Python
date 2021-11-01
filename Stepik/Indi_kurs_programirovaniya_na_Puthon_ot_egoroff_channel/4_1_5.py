# put your python code here
N = int(input())
n = 0
k = 0

while n <= N:
    n = (k + 1)**2
    k = k + 1
    if n <= N:
        print(n)
