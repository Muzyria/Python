# put your python code here
n,m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split()))) # читаем матрицу

for i in range(n):
    print(sum(a[i]), end=' ') # сумируем строки
s = 0    # обнуляем счетчик
print()

for j in range(m): #  считаем значения в столбцах и обнуляем счетчик после вывода
    for i in range(n):
        s += a[i][j]
        
    print(s, end=' ')    
    s = 0