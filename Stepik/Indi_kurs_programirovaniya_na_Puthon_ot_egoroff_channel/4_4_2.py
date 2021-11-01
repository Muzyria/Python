x = int(input())
def isPrime(x):
    if x<2:
        return False
    for i in range(2,x):
        if not x%i:
            return False
    return True  

if isPrime(x) == True:
    print("Yes")
else:
    print("No")