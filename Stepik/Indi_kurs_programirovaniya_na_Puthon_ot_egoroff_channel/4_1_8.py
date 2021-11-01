# put your python code here
n = int(input())
while int(str(n)[0]) != 1:
    n = int(str(n)[0]) * n
    
    if n > 1000000000:
        break
print(n)   