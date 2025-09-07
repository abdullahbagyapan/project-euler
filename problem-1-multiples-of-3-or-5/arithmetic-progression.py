import math

def step(n, m):
    return math.floor((m - 1) / n)

def sum_of_multiples(n, k):
    return n * (k*(k+1))/2


n = 3
m = 1000
k = step(n, m)
k_3 = sum_of_multiples(n, k)

n = 5
m = 1000
k = step(n, m)
k_5 = sum_of_multiples(n, k)


n = 15
m = 1000
k = step(n, m)
k_15 = sum_of_multiples(n, k)


sum = k_3 + k_5 - k_15

print(sum) # Output should be 233168


# Relative links:
# https://en.wikipedia.org/wiki/Arithmetic_progression
# https://en.wikipedia.org/wiki/Set_(mathematics)

