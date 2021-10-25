# put your python code here
a = []
for i in range (5):
    a.append(list(map(int,input().split()))) # читаем матрицу
count = 0
while a[2][2] != 1:
    for i in range (5):
        for j in range (5):
            if a[i][j] == 1: # алгоритм передвижения
                if i<2:
                    a[i+1][j] = a[i][j]
                    a[i][j] = 0
                    count+=1
                elif i>2:
                    a[i-1][j] = a[i][j]
                    a[i][j] = 0
                    count+=1
                elif j>2:
                    a[i][j-1] = a[i][j]
                    a[i][j] = 0
                    count+=1
                elif j<2:
                    a[i][j+1] = a[i][j]
                    a[i][j] = 0
                    count+=1
print (count)