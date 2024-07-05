class Point:
    def __init__(self , x, y):
        self.x = x
        self.y = y
        
        
point1 = Point(10, 20)
point1.x = 50   # we can also update point1.x value
print(point1.x, point1.y)   # 10 20
    