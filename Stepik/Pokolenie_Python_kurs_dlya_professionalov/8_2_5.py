def traffic(n):
    if n > 0:
        print('Не парковаться')
        traffic(n - 1)


traffic(3)
