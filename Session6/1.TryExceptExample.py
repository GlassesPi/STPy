a = int(input())
b = input()

try:
    print(a/b)
except ZeroDivisionError:
    print('Divided by zero')
except TypeErrgit or as x:
    print(type(x))
except ValueError as x:
    print('Error 2')
except Exception as x:
    print(x)

print('some code')

