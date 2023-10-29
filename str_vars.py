s1 = 'abcdefghijk'
print(s1)
print(len(s1))
print(s1[3])
print(s1[:3])
print(s1[-3:])
print(s1[5:8])

s2 = "I can't"
print(s2)
s3 = 'I can\'t "Pawel"'
s3 = "I can't \"Pawel\""
print(s3)
s4 = 'abcsd\nfagwrqgqg'
print(s4)
s5 = 'avabba\tbacc'
print(s5)

print(ord('a'))
print(ord('A'))
print(ord('Ł'))


s4 = 'abcsd\\nfagwrqgqg'
print(s4)
s6 = '523453\tsghgs\t2346326\t326236'
print(s6)
s6a = s6.split('\t')
print(s6a)
print(s6a[2])

print('------------')
s7 = '523453\nsghgs\n2346326\n326236'
print(s7)
s7a = s7.splitlines()
print(s7a)

s8 = 'agabdfdabrt\nsgabfe'

print('count ab: %s' % s8.count('ab'))
# Throws ValueError if not found
print('first occurrence of ab: %s ' % s8.index('ab'))
# Return -1 if not found
print('find ab: %s' % s8.find('abct'))
print('last occurrence of ab: %s ' % s8.rindex('ab'))
rab = s8.rindex('ab')
print(f'last occurrence of ab: {rab} ')
print('last occurrence of ab:' + str(rab))

s9 = '     abcaff agvłąśćóóżżźag     '
print(s9)
print(s9.rstrip())
print(s9.lstrip())
print(s9.strip())