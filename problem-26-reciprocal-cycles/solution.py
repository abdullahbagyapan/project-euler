from sympy import primerange

def multiplicative_order(a, n):
    
    k = 1
    while pow(a, k, n) != 1:
        k += 1
    return k

def reciprocal_cycles(limit):

    longest_cycle = 0
    number = 0

    primes = list(primerange(1, limit))
    primes = filter(lambda _p: _p not in [2, 5], primes) # removing 2 and 5

    for prime in primes:

        cycle_length = multiplicative_order(10, prime)

        if (cycle_length > longest_cycle):
            longest_cycle = cycle_length
            number = prime

    return number, cycle_length


limit = 1_000

number, longest_cycle = reciprocal_cycles(limit)

print(f"The longest cycle is: {longest_cycle}, from: {number}")


# Relative Links:
# https://euler.beerbaronbill.com/en/latest/solutions/26.html