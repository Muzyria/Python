
class Rectangle:
    def __init__(self, *args):
        self.__area = args

    @property
    def area(self):
        return self.__area[0] * self.__area[1]


r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)


print(r1.area) # 15
print(r2.area) # 6 

r1 = Rectangle(10, 50)  
print(r1.area) # 500    