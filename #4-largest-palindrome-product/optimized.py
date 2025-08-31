import math


def is_palindrome(number):
    original = number
    reversed_num = 0
    while number > 0:
        reversed_num = reversed_num * 10 + number % 10
        number //= 10
    return original == reversed_num

def largest_factor_pair(n, min_factor, max_factor):
    for i in range(int(math.isqrt(n)), min_factor - 1, -1):
        if n % i == 0:
            j = n // i
            if min_factor <= j <= max_factor:
                return i, j
    return None

def largest_palindrome_product(max_product, min_product):

    for number in range(max_product, min_product - 1, -1):

        if is_palindrome(number):

            factors = largest_factor_pair(number, min_factor, max_factor)
            if factors is not None:

                return factors


# 3-digit numbers
min_factor = 100
max_factor = 999

# Biggest product of 3-digits number: 999*999
max_product = 998001
# Smallest product of 3-digits number: 100*100
min_product = 10000


a, b = largest_palindrome_product(max_product, min_product)

print(f"Largest factor pair: {a} x {b}")         # Output should be 913 x 993
print(f"Largest factor pair's product: {a*b}")   # Output should be 906609


# Relative links:
# https://en.wikipedia.org/wiki/Integer_factorization
# https://en.wikipedia.org/wiki/Palindrome

