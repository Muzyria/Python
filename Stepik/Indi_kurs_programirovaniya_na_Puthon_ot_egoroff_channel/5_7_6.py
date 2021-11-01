n = int(input())
arr = [list('0' * n) for i in range(n)]  # заполнение списка нулями
k = 0  # переменная для выравнивания, т. е. сужения круга (когда один пройден, увеличение k  на 1)
index = 1  # счётчик
while index < n * n:
    for j in range(k, n - k - 1):  # движение вправо (прямо по индексу j)
        arr[k][j] = index
        index += 1
    for i in range(k, n - k - 1):  # вниз (прямо по индексу i)
        arr[i][n - k - 1] = index
        index += 1
    for j in range(n - k - 1, k, -1):  # влево (обратно по индексу j)
        arr[n - k - 1][j] = index
        index += 1
    for i in range(n - k - 1, k, -1):  # вверх (обратно по индексу i)
        arr[i][k] = index
        index += 1
    k += 1  # круг пройден, увеличиваем k
if arr[n // 2][n // 2] == '0':  # при нечётных n список не заполняет 0 в середине индексом, так что делаем проверку
    arr[n // 2][n // 2] = n * n
[print(*i) for i in arr]  # вывод