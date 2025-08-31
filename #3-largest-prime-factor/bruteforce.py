
def largest_prime_factor(n):

    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n

print(f"Largest prime factor: {largest_prime_factor(600851475143)}") # Output should be 6857

# Relative links:
# https://en.wikipedia.org/wiki/Integer_factorization
# https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic