from sympy.ntheory import factorint

n = 600851475143
factors = factorint(n, use_ecm=True)  # enable ECM
largest_prime_factor = max(factors.keys())

print(f"Largest prime factor: {largest_prime_factor}")  # Output should be 6857

# Relative links:
# https://en.wikipedia.org/wiki/Integer_factorization
# https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
# https://en.wikipedia.org/wiki/Elliptic_curve
# https://en.wikipedia.org/wiki/Lenstra_elliptic-curve_factorization