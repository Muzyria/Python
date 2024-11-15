
class First:
    A = "a"

class Second(First):
    B = "b"


a = Second()

print(a.A)
