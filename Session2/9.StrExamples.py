s = 'adc ef'
s + 'd'
s.index('a')            #0
s.index('z')            #ExceptionError
s.find('a')             #0
s.find('z')             #-1
s.split()               #['adc', 'ef']
s.replace('a','A')      #all
s.count('a')            #1
s.lower()               #'abc ef'
s.upper()               #'ABC EF'
s.isalpha()             #False
s.isdigit()             #False


'a'*3                   #'aaa'

#################################

' '.join(['a','b'])     #a b
len(s)                  #6
'{:0.1f}'.format(1/3)   #0.3
'a:{1}, b:{0}'.format(b,a)
'a{0:0.2f}'

if 'a' in s:

if 'a' not in s: