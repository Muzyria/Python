# put your python code here
n = int(input())
count = 0
count_2 = 0
count_3 = 0
while n != 0:
    last = n % 10
    count += last
    n = n // 10
while count != 0:
    last_2 = count % 10
    count_2 += last_2
    count = count // 10
if count_2 > 9:
    while count_2 != 0:
        last_3 = count_2 % 10
        count_3 += last_3
        count_2 = count_2 // 10
    print(count_3)
else:        
    print(count_2)
    
'''
n = int(input())
while n // 10 > 0:
    n = n // 10 + n % 10
print(n)
'''
