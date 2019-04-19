class Employee:
    def __init__(self, n, s):
        self.name = n
        self.salary = s

    def __str__(self):
        return '{}: {}'.format(self.name, self.salary)

class Programmer(Employee):
    def __init__(self, n, s, l):
        self.language = l
        super().__init__(n, s)

    def __str__(self):
        return super().__str__() + ' :{}'.format(self.language)
        #return '{}: {}: {}'.format(self.name, self.salary, self.language)



e1 = Employee('iman', 10000)
print(e1)
p1 = Programmer('ali', 10 ** 10, 'python')
print(p1)