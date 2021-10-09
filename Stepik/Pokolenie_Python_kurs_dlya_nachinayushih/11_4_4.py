# put your python code here
n = int(input())
li = []
for _ in range(n):
    x = int(input())
    li.append(x)
del li[li.index(min(li))]
del li[li.index(max(li))]
print(*li, sep='\n')
