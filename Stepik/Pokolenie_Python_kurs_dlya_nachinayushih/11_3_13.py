# put your python code here
n = int(input())
li = []
for _ in range(n):
    li.append(input())
index = int(input())    
res = ''
for s in li:
    if len(s) >= index:
        res += s[index - 1]
    
print(res)