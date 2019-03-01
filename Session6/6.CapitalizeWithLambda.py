pascal = lambda a: ''.join([x.title() for x in a.split()])
pascal('first name')

def pascal_long(x):
    s = ''
    for a in x.split():
        a += a.title()
    return ''.join(s)