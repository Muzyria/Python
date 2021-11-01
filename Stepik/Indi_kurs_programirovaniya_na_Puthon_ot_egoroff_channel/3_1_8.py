# put your python code here
a, b, c = int(input()), int(input()), int(input())
print('YES' if a + b > c and a + c > b and b + c > a else 'NO')