import math

def proper_divisors(n: int) -> list[int]:
    
    divisors = [1]
    limit = int(math.isqrt(n))

    for i in range(2, limit + 1):
    
        if n % i == 0:
            divisors.append(i)
    
            if i != n // i:  # avoid duplicates
                divisors.append(n // i)

    return divisors


def amicable_numbers(limit: int) -> int:
    
    divisor_sums = {}
    amicables = set()
    
    for i in range(2, limit + 1):
    
        if i not in divisor_sums:
            divisor_sums[i] = sum(proper_divisors(i))
        
        d = divisor_sums[i]
        
        if d != i and d <= limit:  # must not be perfect number
        
            if d not in divisor_sums:
                divisor_sums[d] = sum(proper_divisors(d))
            
            if divisor_sums[d] == i:  # amicable pair found
                amicables.add(i)
                amicables.add(d)

    return sum(amicables)


n = 10_000
print(amicable_numbers(n))  # Expected result: 31626
