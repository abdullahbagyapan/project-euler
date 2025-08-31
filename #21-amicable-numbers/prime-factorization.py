from sympy import factorint

def proper_divisors_sum(n):
    
    factors = factorint(n)
    
    total = 1
    
    for p, exp in factors.items():
        
        total *= (p**(exp+1) - 1) // (p - 1)  # sum of all divisors
    
    return total - n

def amicable_numbers(limit):
    
    checked = set()
    amicables = set()

    for i in range(2, limit + 1):
        
        if i in checked:
            continue
        
        sum_div = proper_divisors_sum(i)
        
        if sum_div != i and proper_divisors_sum(sum_div) == i:
            
            amicables.add(i)
            amicables.add(sum_div)
            
            checked.add(i)
            checked.add(sum_div)

    return sum(amicables)

n = 10_000
print(amicable_numbers(n))  # Output: 31626
