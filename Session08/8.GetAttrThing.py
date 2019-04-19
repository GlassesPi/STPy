class C:
    def __init__(self):
        value = 5
    def func(self):
        print('Hello')

c = C()
print(getattr(c, 'value'))
getattr(c, 'func')()