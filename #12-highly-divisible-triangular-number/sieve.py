def sieve(n):
    """Return a list of primes up to n inclusive."""
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [p for p in range(2, n+1) if sieve[p]]

def prime_factorization(n, primes):
    """Return a dict of prime factors and their exponents for n."""
    factors = {}
    for p in primes:
        if p*p > n:
            break
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        if count > 0:
            factors[p] = count
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def count_divisors_from_factors(factors):
    """Calculate number of divisors from prime factorization dict."""
    count = 1
    for exp in factors.values():
        count *= (exp + 1)
    return count

def count_divisors(n, primes):
    factors = prime_factorization(n, primes)
    return count_divisors_from_factors(factors)

def triangular_number_divisors(min_divisors):
    # Estimate max number for sieve (can be tuned)
    max_num = 10**2  
    primes = sieve(max_num)
    
    i = 1
    while True:
        if i % 2 == 0:
            count1 = count_divisors(i // 2, primes)
            count2 = count_divisors(i + 1, primes)
        else:
            count1 = count_divisors(i, primes)
            count2 = count_divisors((i + 1) // 2, primes)
        
        divisors = count1 * count2
        if divisors >= min_divisors:
            triangular_number = i * (i + 1) // 2
            return triangular_number
        i += 1

number = triangular_number_divisors(500)
print(f"Triangular number: {number}")