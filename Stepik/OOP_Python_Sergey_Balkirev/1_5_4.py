class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y =y
        self.color = color


points = [Point(i, i) for i in  range(1,2000,2)] 
points[1] = Point(3, 3, "yellow") 


"""
class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color
        
points = [Point(i, i) for i in range(1, 2001, 2)]
points[1].color = 'yellow'   
"""