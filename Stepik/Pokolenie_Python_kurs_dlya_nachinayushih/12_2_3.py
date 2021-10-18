# put your python code here
l = [int(i) for i in input().split()]
print(*l, sep='+', end='')
print('=', sum(l), sep='')