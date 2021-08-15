
a=int(input())
b=int(input())
c=int(input())
d=int(input())

for z in range(c,d+1): # Выводим шапку таблицы
    print('\t',z, end='')
print() 

for x in range(a,b+1):
    print(x, end='\t')
    for y in range(c,d+1): 
        print(x*y, end='\t')
    print()