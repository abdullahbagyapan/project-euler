import random
import math

# ---- Basic helpers ----
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def montgomery_add(XP, ZP, XQ, ZQ, X_diff, Z_diff, N):
    """Montgomery differential addition: P + Q given P-Q"""
    t1 = (XP - ZP) * (XQ + ZQ) % N
    t2 = (XP + ZP) * (XQ - ZQ) % N
    t3 = (t1 + t2) % N
    t4 = (t1 - t2) % N
    X = (Z_diff * t3 * t3) % N
    Z = (X_diff * t4 * t4) % N
    return X % N, Z % N

def montgomery_double(XP, ZP, A24, N):
    """Montgomery point doubling"""
    t1 = (XP + ZP) % N
    t2 = (XP - ZP) % N
    t1 = t1 * t1 % N
    t2 = t2 * t2 % N
    X2 = (t1 * t2) % N
    Z2 = ((t1 - t2) * A24 + t2) % N
    Z2 = (Z2 * (t1 - t2)) % N
    return X2, Z2

# ---- Scalar multiplication (Montgomery ladder) ----
def montgomery_ladder(k, X1, Z1, A24, N):
    R0 = (1, 0)
    R1 = (X1, Z1)
    for bit in reversed(bin(k)[2:]):
        if bit == '1':
            R0, R1 = montgomery_add(*R0, *R1, X1, Z1, N), montgomery_double(*R1, A24, N)
        else:
            R1, R0 = montgomery_add(*R0, *R1, X1, Z1, N), montgomery_double(*R0, A24, N)
    return R0

# ---- ECM Stage-1 with Montgomery curves ----
def ecm_stage1_mont(N, B1=5000, trials=20):
    """Stage-1 ECM using Montgomery curves"""
    primes = [p for p in range(2, B1+1) if all(p % d != 0 for d in range(2, int(p**0.5)+1))]
    for _ in range(trials):
        # Random Montgomery curve: By^2 = x^3 + Ax^2 + x, we only need X-coordinate
        x0 = random.randrange(1, N)
        A = random.randrange(1, N)
        A24 = (A + 2) * pow(4, -1, N) % N  # A24 = (A+2)/4 mod N
        X, Z = x0, 1
        try:
            for p in primes:
                e = 1
                while p**(e+1) <= B1:
                    e += 1
                k = p**e
                X, Z = montgomery_ladder(k, X, Z, A24, N)
        except ZeroDivisionError:
            f = gcd(Z, N)
            if 1 < f < N:
                return f
    return None

# ---- Full factorization using Montgomery ECM ----
def ecm_factor_full_mont(N):
    to_factor = [N]
    factors = []
    while to_factor:
        n = to_factor.pop()
        if n <= 1:
            continue
        f = ecm_stage1_mont(n, B1=5000, trials=50)
        if f is None:
            # fallback trial division
            fs = []
            for p in range(2, int(n**0.5)+1):
                while n % p == 0:
                    fs.append(p)
                    n //= p
            if n > 1:
                fs.append(n)
            factors.extend(fs)
        else:
            to_factor.append(f)
            to_factor.append(n//f)
    factors.sort()
    return factors

N = 600851475143

factors = ecm_factor_full_mont(N)

print(f"Largest prime factor: {max(factors)}") # Output should be 6857



# Relative links:
# https://en.wikipedia.org/wiki/Integer_factorization
# https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
# https://en.wikipedia.org/wiki/Elliptic_curve
# https://en.wikipedia.org/wiki/Montgomery_curve
# https://en.wikipedia.org/wiki/Lenstra_elliptic-curve_factorization