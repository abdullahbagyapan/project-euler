import math

def nth_prime(n):

    primes = [2]
    candidate = 3
    
    while len(primes) < n:
        is_prime = True
        sqrt_candidate = math.isqrt(candidate)
        for p in primes:
            if p > sqrt_candidate:
                break
            if candidate % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2  # skip even numbers
    
    return primes[-1]

N = 10001

prime = nth_prime(N)

print(f"{N}'th prime is: {prime}")   # Output should be 104743


# Relative links:
# https://en.wikipedia.org/wiki/Prime_number