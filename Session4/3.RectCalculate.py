from math import atan
class ComplexNum:
    def __init__(self, x, y):
        self.width = x
        self.height = y
    
    def __eq__(self, other):
        h = False
        if (self.width == other.width) and (self.height == other.height):
            h = True
        return h

c1 = ComplexNum(int(input("Enter rectangle's X: ")), int(input("Enter rectangle's Y: ")))
c2 = ComplexNum(int(input("Enter rectangle's X: ")), int(input("Enter rectangle's Y: ")))

print(c1 == c2)
