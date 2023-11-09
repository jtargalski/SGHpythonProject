num_list = [2, 5, 7, 9, 11, 13, 18]

'''
TODO 
1. Print the subsequent 2nd powers of elements in the list
2. Sum the 2nd powers of elements of the list
'''

sum_of_num_sqr = 0
for num in num_list:
    num_to_pow = num**2
    print (num_to_pow)
    sum_of_num_sqr += num_to_pow

print(sum_of_num_sqr)

num_list_pow = [x**2 for x in num_list]
print(num_list_pow)

sum_sqr = 0
for el in num_list_pow:
    sum_sqr += el

print(sum)

