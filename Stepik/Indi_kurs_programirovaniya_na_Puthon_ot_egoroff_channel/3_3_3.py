# put your python code here
a, b, c = int(input()), int(input()), int(input())
if a == b == c and a == c == b:
    print(3)
elif a != b != c and a != c != b:
    print(0)
else:
    print(2)