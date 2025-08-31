import math
import random

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    if n == 1:
        return 1
    if is_prime(n):
        return n

    while True:
        x = random.randrange(2, n)
        y = x
        c = random.randrange(1, n)
        d = 1
        f = lambda x: (x*x + c) % n

        while d == 1:
            x = f(x)
            y = f(f(y))
            d = math.gcd(abs(x - y), n)

        if d != n:
            return d

# ---- Simple primality check ----
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# ---- Recursive factorization ----
def factorize(n):
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    factor = pollards_rho(n)
    return factorize(factor) + factorize(n // factor)


N = 600851475143

factors = factorize(N)

print("Largest prime factor:", max(factors)) # Output should be 6857


# Relative links:
# https://en.wikipedia.org/wiki/Integer_factorization
# https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
# https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm