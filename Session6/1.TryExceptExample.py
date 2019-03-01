a = int(input())
b = input()

raise IOError
try:
    print(a/b)
except ZeroDivisionError:
    print('Divided by zero')
except TypeError as x:
    print(type(x))
except ValueError as x:
    print('Error 2')
except Exception as x:
    print(x)

print('some code')

