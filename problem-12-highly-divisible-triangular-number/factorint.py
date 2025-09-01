from sympy import factorint

def generate_triangular_number(n):
    
    number = (n * (n+1)) / 2
    return int(number)
    

def count_divisors(n):
    factors = factorint(n)  # Returns dict {prime_factor: exponent}
    count = 1
    for exponent in factors.values():
        count *= (exponent + 1)
    return count

def triangular_number_divisors(n):
    
    i = 1
    divisors = 0
    triangular_number = 0
    
    while (divisors < n):
        
        triangular_number = generate_triangular_number(i)
        divisors = count_divisors(triangular_number)
        
        i += 1
        
    return triangular_number
        
    
triangular_number = triangular_number_divisors(500)

print(triangular_number)
