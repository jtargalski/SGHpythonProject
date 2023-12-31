from time import time

from bowls import sum_of_bowls_loop, sum_of_bowls_recursive, sum_of_bowls_sequence


def time_func(func, n):
    t0 = time()
    print('Calling: {} for n={}'.format(func.__name__, n))
    print('Res={}'.format(func(n)))
    t1 = time()
    elapsed = t1 - t0
    print(f'It took: {elapsed} sec')


n = 1000000
time_func(sum_of_bowls_loop, n)
time_func(sum_of_bowls_sequence, n)
time_func(sum_of_bowls_recursive, n)

