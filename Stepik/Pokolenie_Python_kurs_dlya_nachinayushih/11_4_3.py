# put your python code here
n = int(input())
li = []
for _ in range(n):
    x = int(input())
    li.append(x)
    print(x)
print()
for i in li:
    s = i ** 2 + i * 2 +1
    print(s)