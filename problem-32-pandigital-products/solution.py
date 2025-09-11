import itertools

def pandigital_products():

    products = set()
    
    digits = '123456789'
    
    permutations = itertools.permutations(digits)

    for p in permutations:

        # Case 1: 1-digit × 4-digit = 4-digit
        a = int(''.join(p[0:1]))
        b = int(''.join(p[1:5]))
        c = int(''.join(p[5:9]))
        if a * b == c:
            products.add(c)
        
        # Case 2: 2-digit × 3-digit = 4-digit
        a = int(''.join(p[0:2]))
        b = int(''.join(p[2:5]))
        c = int(''.join(p[5:9]))
        if a * b == c:
            products.add(c)
    
    return products

pandigital_numbers = pandigital_products()

print(f"The pandigitsal numbers are: {pandigital_numbers}")                 # The output should be {5346, 5796, 6952, 4396, 7852, 7632, 7254}

print(f"The sum of the pandigital numbers is: {sum(pandigital_numbers)}")   # The output should be 45228
