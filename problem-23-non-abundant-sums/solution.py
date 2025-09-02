import math


def proper_divisors(n):
    
    divisors = [1]
    limit = int(math.isqrt(n))

    for i in range(2, limit + 1):
    
        if n % i == 0:
            divisors.append(i)

            if i != n // i:  # avoid duplicates
                divisors.append(n // i)

    return divisors


def get_abundant_numbers(lower_limit, upper_limit):

    abundants = []

    for i in range(lower_limit, upper_limit):

        sum_of_divisors = sum(proper_divisors(i))

        if (i < sum_of_divisors):
            abundants.append(i)

    return abundants


def non_abundant_sums(lower_limit, upper_limit):

    abundants = get_abundant_numbers(lower_limit, upper_limit)
        
    arr = bytearray(upper_limit + 1)

    for i, a in enumerate(abundants):

        for b in abundants[i:]:
            s = a + b
            if s > upper_limit: break
            arr[s] = 1

    return sum(i for i in range(1, len(arr)) if not arr[i])



upper_limit = 28_123
lower_limit = 12

sum_of_the_non_abundants = non_abundant_sums(lower_limit, upper_limit)

print(f"The sum of the non abundant numbers is: {sum_of_the_non_abundants}") # 4179871


# Relative Links:
# https://en.wikipedia.org/wiki/Abundant_number