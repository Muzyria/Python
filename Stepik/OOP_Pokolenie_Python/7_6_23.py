def get_method_owner(cls, method):
    for i in cls.mro():
        if method in i.__dict__:
            return i


class A:
    def m(self):
        pass


class B(A):
    pass


print(get_method_owner(B, 'm'))