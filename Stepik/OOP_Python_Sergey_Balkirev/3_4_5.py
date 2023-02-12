class NewList:
    def __init__(self, lst: list = None):
        self.lst = [] if lst is None else lst

    def get_list(self):
        return self.lst

    @classmethod
    def __get_new_list(cls, lst1, lst2):
        d1 = [(i, type(i)) for i in lst1]
        d2 = [(i, type(i)) for i in lst2]
        for i in d2:
            if i in d1:
                d1.remove(i)
        return [i[0] for i in d1]

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError("Операторы должны быть list или NewList")

        second_lst = other
        if isinstance(other, NewList):
            second_lst = other.lst
        return NewList(self.__get_new_list(self.lst, second_lst))

    def __rsub__(self, other):
        new_obj = NewList(other)
        return new_obj - self

    def __isub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError("Операторы должны быть list или NewList")

        second_lst = other
        if isinstance(other, NewList):
            second_lst = other.lst

        self.lst = self.__get_new_list(self.lst, second_lst)
        return self


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(res_1)

# lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
# res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
# res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
