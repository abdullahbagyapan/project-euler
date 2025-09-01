import math


def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
    
def smallest_multiple(N):
    
    product = 1
    
    for i in range(N):
        
        if is_prime(i):
            
            power = int(math.log(N, i))
            product = product * (i**power)
            
    return product
    
N = 20

product = smallest_multiple(N)

print(f"Smallest Multiple's product: {product}")   # Output should be 232792560


# Relative links:
# https://en.wikipedia.org/wiki/Prime_power
