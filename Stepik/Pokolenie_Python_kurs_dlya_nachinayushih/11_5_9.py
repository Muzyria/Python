# put your python code here
n = input().split()

for i in range(len(n)):
    n[i] = int(n[i])
s = 0

for i in range(len(n)):
    for w in range(i +1, len(n)):
        if n[i] == n[w]:
            s += 1
print(s)        