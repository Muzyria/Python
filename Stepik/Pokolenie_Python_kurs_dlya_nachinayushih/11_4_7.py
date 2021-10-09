# put your python code here
n = int(input())
li = []
li2 = []
li3 = []
count = 0
for _ in range(n):
    x = input()
    li.append(x)
    
q = int(input())
for _ in range(q):
    k = input()
    li2.append(k)
    
for i in li:
    count = 0
    for j in li2:
        if j.lower() in i.lower():
            count += 1
        if count == q:
            li3.append(i)         
print(*li3, sep='\n')

'''
# put your python code here
n = int(input())
m1, m2, count = [], [], 0
for _ in range(n):
    m1.append(input())
k = int(input())
for _ in range(k):
    m2.append(input())
for i in m1:
    count = 0
    for j in m2:
        if str.lower(j) in str.lower(i):
            count += 1
            if count == len(m2):
                print(i)
'''