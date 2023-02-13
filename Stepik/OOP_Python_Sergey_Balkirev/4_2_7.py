class Tuple(tuple):
    def __add__(self, iter_obj):
        return Tuple(tuple(self) + tuple(iter_obj))


if __name__ == '__main__':
    t = Tuple([1, 2, 3])
    t = t + "Python"
    print(t)  # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
    t = (t + "Python") + "ООП"
