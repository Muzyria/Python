# put your python code here
n =int(input())
mish = 0
play = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        mish += 1
    else:
        play += 1
if mish > play:
    print('Mishka')
elif mish == play:
    print('Friendship is magic!^^')
else:
    print('Chris')