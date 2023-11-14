# Please write a program that prints the first N prime numbers.
# N should be declared as a variable at the beginning of your code or provided as input from the user.


# N defines the number of first prime numbers to be printed
N = int(input("How many first prime numbers do you want to print?: "))

# Below is the first solution based on two functions

"""
def prime_checker(number):
    n = int(number)
    is_prime = True
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for denominator in range(2, (int(n**0.5) + 1)):  # range based on trial division test for primality
            if n % denominator == 0:
                is_prime = False
        if is_prime:
            return True
        else:
            return False

def print_first_n_primes(x):
    count = 0  # used to count the number of already printed prime numbers
    num = 2  # starts from 2, because it is known that 1 is not a prime number
    while count < x:
        if prime_checker(num):  # checks if value is
            print(num)
            count += 1
        num += 1

print_first_n_primes(N)
"""

# this is the second possible solution written in one function and the code is shorter in general
# based on checking whether a number is divisible by any prime number that is already on the list
def first_n_prime_nums(x):
    prime_numbers = []
    number = 2
    is_prime = True
    while len(prime_numbers) < x:
        test_if_prime = []
        for i in prime_numbers:
            if number % i == 0:
                test_if_prime += [number]
        if test_if_prime:                    # if list is not empty then it is True, and the number is not prime
            prime_numbers += []
        else:
            prime_numbers += [number]
        number += 1
    return prime_numbers


print(first_n_prime_nums(N))