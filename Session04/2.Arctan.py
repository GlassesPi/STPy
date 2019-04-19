from math import atan
class ComplexNum:
    def __init__(self, x, y):
        self.real = x
        self.imaginary = y

    def phase(self):
        return atan(self.imaginary / self.real)
    
    def __str__(self):
        return "Real number is {}, imaginary one is {} and atan is {}".format(self.real, self.imaginary, self.phase())

    def __add__(self, other):
        q = self.real + other.real
        w = self.imaginary + other.imaginary

        return ComplexNum(q, w)

c1 = ComplexNum(int(input("Enter real Num: ")), int(input("Enter imaginary Num: ")))
c2 = ComplexNum(int(input("Enter real Num: ")), int(input("Enter imaginary Num: ")))

print(c1 + c2)
