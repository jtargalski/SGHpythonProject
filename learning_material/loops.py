for i in range(0, 5):
    print(f'i={i}')
print('----------')
for i in range(0, 5, 2):
    print(f'i={i}')

print('----------')
for i in reversed(range(-5, 10, 2)):
    print(f'i={i}')

print('----------')
for i in 'abcdded':
    print(f'i={i}')

print('----------')
w = 2
while w < 10:
    w = w + 1
    if w == 4:
        continue
    if w == 8:
        break
    print(f'w={w}')
    #w += 1
