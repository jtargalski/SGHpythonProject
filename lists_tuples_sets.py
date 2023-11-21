num_list = [2, 7, 5, 15, 7, 9, 11, 5, 13, 18]
num_list_pow = [ x**2 for x in num_list ]
print(num_list_pow)
num_list_pow_sorted = sorted(num_list_pow)
print(num_list_pow_sorted)
num_list_pow_sorted_rev = sorted(num_list_pow, reverse=True)
print(num_list_pow_sorted_rev)
print('--- set ---')
num_list_pow_set = set(num_list_pow)
print(num_list_pow_set)

num_list_pow_unique = sorted(list(set(num_list_pow)))
print(num_list_pow_unique)

print('--- tuples ---')
tuple_list = [(1,2), (2,4), (0,8), (5,4)]
x, y = tuple_list[0]
print(x, y)
t = (1, 5, 6)
print(t[1])
t[1] = 6 #you cannot change an existing tuple, this will result in an error

print('--- matrix ---')

list_2D = [[1, 2, 4], [2, 4, 3], [0, 0, 1], [5, 4, 0]]
print(list_2D)


for row in list_2D:
    print(row)

print(list_2D[0][0] + list_2D[0][1] + list_2D[0][2])
print(list_2D[1][0] + list_2D[1][1] + list_2D[1][2])
print(list_2D[2][0] + list_2D[2][1] + list_2D[2][2])
print(list_2D[3][0] + list_2D[3][1] + list_2D[3][2])

row_sum = []
for row in list_2D:
    row_sum.append(sum(row))
print(row_sum)

print(sum(row_sum))

#sum all columns in list_2D

n_col = len(list_2D[0])
print(n_col)


list_2D = [[1, 2, 4], [2, 4, 3], [0, 0, 1], [5, 4, 0]]

sum_of_col = [0] * n_col
print(sum_of_col)

for row in list_2D:
    col_sum = 0
    for n in range(n_col):
        sum_of_col[n] += row[n]

print(sum_of_col)








