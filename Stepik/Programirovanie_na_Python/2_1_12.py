a = int(input())
b = int(input())
d = min(a,b)
while d % max(a,b) !=  0:
    d += min(a,b)
print(d) 