n = int(input())
count = 0
while n>1:

    if n % 2 != 0:
        count +=1
        n = (3*n)+1
        
    if n % 2 == 0:
        count += 1
        n = n / 2
print(count)