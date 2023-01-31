
class Quadrilateral:
    def __init__(self, width,  height=None):
        self.width = width
        if height == None:
            self.height = self.width
        else:    
            self.height = height            

    def __str__(self):
        if self.width == self.height:
            return f"Куб размером {self.width}х{self.height}"
        else:
            return f"Прямоугольник размером {self.width}х{self.height}"

    def __bool__(self):
        return self.height == self.width          



q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False"


"""
class Quadrilateral:
    def __init__(self, *args):
        self.width = args[0]
        self.height = args[1] if len(args) > 1 else args[0]

    def __str__(self):
        if self.__bool__():
            return f'Куб размером {self.width}х{self.height}'
        return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return self.width == self.height
"""

            
