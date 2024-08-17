
def my_rec(x: list[int]) -> int:
    if len(x) == 1:
        return x[0]
    return x[0] * my_rec(x[1:])


if __name__ == '__main__':
    print(my_rec(list(range(1, 10))))
