import math
import numpy as np
from sympy import isprime

# ---- Build factor base ----
def build_factor_base(N, B_bound=300):
    return [p for p in range(2, B_bound+1) if isprime(p) and pow(N, (p-1)//2, p) == 1]

# ---- Check if number is B-smooth ----
def is_B_smooth(n, factor_base):
    if n < 0: n = -n
    exponents = []
    for p in factor_base:
        count = 0
        while n % p == 0:
            n //= p
            count += 1
        exponents.append(count)
    return exponents if n == 1 else None

# ---- Quadratic Sieve stage-1: optimized ----
def quadratic_sieve_factor(N, B_bound=300, M=3000):
    factor_base = build_factor_base(N, B_bound)
    x0 = int(math.isqrt(N)) + 1
    smooth_relations = []
    x_list = []

    # Collect smooth numbers using sieving
    for k in range(M):
        x = x0 + k
        y = x*x - N
        exp_vec = is_B_smooth(y, factor_base)
        if exp_vec:
            smooth_relations.append([e % 2 for e in exp_vec])
            x_list.append(x)
        if len(smooth_relations) > len(factor_base):
            break

    if len(smooth_relations) <= len(factor_base):
        return None

    # ---- Linear algebra mod 2 using numpy ----
    A = np.array(smooth_relations, dtype=int).T
    rows, cols = A.shape

    # Gaussian elimination mod 2 to find approximate nullspace
    for i in range(min(rows, cols)):
        pivots = np.where(A[i, i:] == 1)[0]
        if pivots.size == 0:
            continue
        pivot = pivots[0] + i
        if pivot != i:
            A[:, [i, pivot]] = A[:, [pivot, i]]
        for j in range(i+1, cols):
            if A[i, j] == 1:
                A[:, j] = (A[:, j] + A[:, i]) % 2

    null_vec = A[:, -1]  # last column as nullspace vector

    # Compute X and Y
    X_prod = 1
    Y_factors = [0]*len(factor_base)
    for idx, bit in enumerate(null_vec):
        if bit:
            X_prod *= x_list[idx]
            for i in range(len(factor_base)):
                Y_factors[i] += smooth_relations[idx][i]
    Y_prod = 1
    for i, p in enumerate(factor_base):
        Y_prod *= p**(Y_factors[i]//2)

    factor = math.gcd(X_prod - Y_prod, N)
    if 1 < factor < N:
        return factor
    return None

# ---- Recursive largest prime factor ----
def largest_prime_factor(N):
    
    if isprime(N):
        return N
    
    factor = quadratic_sieve_factor(N, B_bound=400, M=4000)
    
    if not factor:
        # fallback trial division
        for p in range(2, int(math.isqrt(N))+1):
            if N % p == 0:
                factor = p
                break
    
    if not factor or factor == N:
        return N
    
    return max(largest_prime_factor(factor), largest_prime_factor(N//factor))


N = 600851475143

largest = largest_prime_factor(N)

print(f"Largest prime factor: {largest}") # Output should be 6857


# Relative links:
# https://en.wikipedia.org/wiki/Integer_factorization
# https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
# https://en.wikipedia.org/wiki/Quadratic_sieve