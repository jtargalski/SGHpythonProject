p = False
q = True

# https://introcs.cs.princeton.edu/java/71boolean/images/truth-table.png

if p and q:
    print('p and q True')
else:
    print('p and q False')

if p or q:
    print('p or q True')
else:
    print('p or q False')

#XOR
if p ^ q:
    print('p xor q True')
else:
    print('p xor q False')

if not p and q:
    print('not p and q True')
else:
    print('not p and q False')


print('-------------')
a = 10
b = 10

if a > b:
    print('a>b')
else:
    print('not a>b')

if a == b:
    print('a=b')
else:
    print('not a=b')

if a >= b:
    print('a>=b')
else:
    print('not a>=b')

s1 = 'abc'
s2 = 'abcf'

# not equal
if s1 != s2:
    print('s1!=s2')

y = 100 if s1==s2 else 10
print(y)


mv = 200

match mv:
    case 100:
        print('mv=100')
    case 200:
        print('mv=200')
    case _:
        print('mv is different')