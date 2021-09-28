# put your python code here
n = int(input())
i = 0
while i != n:
    i += 1
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)