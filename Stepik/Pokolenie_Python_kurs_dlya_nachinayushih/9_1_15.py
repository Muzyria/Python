n = int(input()) 
d = ''            
while n > 0:
    d = str(n % 2) + d  
    n //= 2
print(d)
