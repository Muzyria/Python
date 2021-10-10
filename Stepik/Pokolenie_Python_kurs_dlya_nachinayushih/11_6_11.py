l = []
for i in input().split():
    l.append(int(i))
l.sort()
print(*l)
l.sort(reverse = True)
print(*l)

'''
# put your python code here
n = input().split()
for i in range(len(n)):
    n[i] = int(n[i])
n.sort()
print(*n)
n.sort(reverse = True)
print(*n)

'''