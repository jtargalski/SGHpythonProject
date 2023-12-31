#   * * * * * *
#    * * * * *
#     * * * *
#      * * *
#       * *
#        *

n = 6
#TODO given n - number of rows write a function that gives the
# sum of all bowls

sum_of_bowls = sum([x for x in range(1, n+1)])

def sum_of_bowls_sequence(n):
    return n * (n+1)/2

def sum_of_bowls(n):
    return sum([x for x in range(1, n+1)])

print(sum_of_bowls(n))
print(sum_of_bowls_sequence(n))
