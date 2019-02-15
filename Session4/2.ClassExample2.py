from math import atan
class ComplexNum:
    def __init__(self, x, y):
        self.real = x
        self.imaginary = y

    def phase(self):
        return atan(self.imaginary / self.real)

c = ComplexNum(int(input("Enter real Num: ")), int(input("Enter imaginary Num: ")))
print(c.phase())
