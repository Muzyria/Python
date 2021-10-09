# put your python code here
n = int(input())
li = []
for _ in range(n):
    x = input()
    li.append(x)
k = input()
for i in li:
    if k.lower() in i.lower():
        print(i, sep='\n')