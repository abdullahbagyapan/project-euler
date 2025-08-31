import math

def lattice_paths(n):
    
    return math.factorial(2*n) // (math.factorial(n)**2)


n = 20

result = lattice_paths(n)

print(result)