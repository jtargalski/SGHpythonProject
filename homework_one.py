# Please write a program that prints the first N prime numbers.
# N should be declared as a variable at the beginning of your code or provided as input from the user.
# You can attach a file here in the assignment or you can submit it as a link to your file on github.
# If you'd like to add any explanation of your code, please add it to the file in a comment,
# don't use the textfield when submitting the assignment.




N = int(input("Enter the number: ")) #N defines the number of first prime numbers to be printed


def prime_checker(number):
    n = int(number)
    is_prime = True
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for denominator in range(2, (round(n/2) + 1)):  # range for efficiency to not check double the numbers
            remainder = n % denominator
            if remainder == 0:
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


