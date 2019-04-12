class Shape:
    @staticmethod #Decorator
    def factory(tp, **kwargs):
        if tp.lower() == "circle": return Circle(**kwargs)
        if tp.lower() == "rectangle": return Rectangle(**kwargs)

class Circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius ** 2 * 3.14

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y


c = Shape.factory('CIRCLE', r=5)
print(c.area())
r = Shape.factory('rectangle', x=3, y=6)
print(r.area())