class Circle:
    def __init__(self, r):
        self.radius = r

class Rect:
    def __init__(self, x, y):
        self.w = x
        self.h = y
    
    def Area(self):
        return self.w * self.h

c = Circle(int(input("Enter circle's stuff: ")))
print("The circle's radius is {}".format(c.radius))

d = Rect(int(input("Enter rectangle's X: ")), int(input("Enter rectangle's Y: ")))
print("The rectangle's X is {}, its Y is {} and area of that is {}".format(d.h, d.w, d.Area()))