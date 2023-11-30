my_file = 'numbers.csv'
with open(my_file, 'r') as f:
    lines = f.readlines()
    i = 0
    for line in lines:
        i += 1
        print(f'{i}: {line}', end='')

print('\n')

el1 = lines[0].split(';')
el2 = lines[1].split(';')
el3 = lines[2].split(';')

el1[2] = el1[2][:-1]
el2[2] = el2[2][:-1]

for n in range(0, len(el1)):
    el1[n] = int(el1[n])
    el2[n] = int(el2[n])
    el3[n] = int(el3[n])

list_2D = [el1, el2, el3]

row_sum = []
for row in list_2D:
    row_sum.append(sum(row))
print(f'Sum of rows is {row_sum}')

col_sum = [0, 0, 0]
for row in list_2D:
    for i in range(len(row)):
        col_sum[i] += row[i]

print(f'Sum of columns is {col_sum}')

print(f'Sum of all is {sum(row_sum)}')
