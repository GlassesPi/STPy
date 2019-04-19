class NamingStrategy:
    def __init__(self, func):
        self.func = func
    def execute(self, arg):
        if self.func == 'underlined':
            return self.underlined(arg)
        elif self.func == 'pascal':
            return self.pascal(arg)
        else:
            return arg
    def underlined(self, a):
        return a.replace(' ', '_')
    def pascal(self, a):
        return ''.join([x.capitalize() for x in a.split()])
        
strat1 = NamingStrategy('underlined')
print(strat1.execute('first name'))
strat2 = NamingStrategy('pascal')
print(strat2.execute('some thing'))