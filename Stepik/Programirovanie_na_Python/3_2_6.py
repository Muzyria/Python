# put your python code here
n='' #инициализация строки
n = str(input())
m = [] #инициализация списка
m.append([str(s.lower()) for s in n.split()]) 
d = {} #инициализация пустого словаря
li, lj = len(m), len(m[0])
for i in range(li):
    for j in range(lj):
        p = m[i][j]
        if p in d:
            d[p]+=1
        else:
            d[p] = 1
for key,value in d.items():
   print(key,value)