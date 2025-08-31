import numpy as np

def sieve(n):

    # Only odd numbers, index i represents number 2*i + 3
    size = (n - 3) // 2 + 1
    is_prime = np.ones(size, dtype=bool)

    for i in range(int(n**0.5)//2 + 1):

        if is_prime[i]:
            p = 2*i + 3
            start = (p*p - 3)//2
            is_prime[start::p] = False

    primes_sum = 2 + np.sum((2*np.nonzero(is_prime)[0] + 3))
    
    return primes_sum


N = 2_000_000

sum_of_primes = sieve(N)

print(f"Sum of primes to {N}-th number: {sum_of_primes}")       # Output should be 142913828922


# Relative Links:
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
