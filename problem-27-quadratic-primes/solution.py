from sympy import isprime, primerange


def f(n, a, b):
    return n * n + a * n + b


def quadratic_primes(limit):

    best = (-1, 0, 0)  # (length, a, b)

    primes = list(primerange(2, limit + 1))  # Generate primes up to 'limit'

    # b must be prime
    for b in primes:

        # If b is not 2, make 'a' odd to ensure f(n) stays odd
        increment = 2 if b != 2 else 1

        for a in range(1 - limit, limit, increment):

            length = 0
            while True:
                result = f(length, a, b)
                if result < 2 or not isprime(result):
                    break
                length += 1

            if length > best[0]:
                best = (length, a, b)

    return best


limit = 1000

length, a, b = quadratic_primes(limit)

print(f"The longest length is: {length}, a: {a}, b: {b}")
print(f"The product of a and b is: {a*b}")

