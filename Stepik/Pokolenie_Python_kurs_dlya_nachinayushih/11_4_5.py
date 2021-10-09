# put your python code here
n = int(input())
li = []
for _ in range(n):
    x = input()
    if x not in li:
        li.append(x)
    else:
        continue

print(*li, sep='\n')