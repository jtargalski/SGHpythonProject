#   * * * * * *
#    * * * * *
#     * * * *
#      * * *
#       * *
#        *

n = 6
#TODO given n - number of rows write a function that gives the
# sum of all bowls

def sum_of_bowls_sequence(n):
    return n * (n + 1)/2

def sum_of_bowls_loop(n):
    return sum([x for x in range(1, n+1)])


def sum_of_bowls_recursive(n):
    if n == 1:
        return 1
    else:
        res = sum_of_bowls_recursive(n - 1) + n
        return res


if __name__ == '__main__':
    print('Sum using sequences: {}'.format(sum_of_bowls_sequence(n)))
    print('Sum using loop: {}'.format(sum_of_bowls_loop(n)))
    print('Sum using recursion: {}'.format(sum_of_bowls_recursive(n)))
