# считывание строки и разбиение ее по пробелам
lst_in = input().split()


def check_int(x):
    try:
        int(x)
        return True
    except Exception:
        return False


print(sum([int(i) for i in lst_in if check_int(i)]))
