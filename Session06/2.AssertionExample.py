a = int(input())
b = int(input())

assert b != 0

try:
    assert 2 + 2 == 4, 'End of world'
except AssertionError as x:
    print(x)

print('hooray')