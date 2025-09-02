import math

def nth_lexicographic_permutation(elements, n):
    """
    Returns the n-th lexicographic permutation (1-indexed)
    of the given sorted list of elements.
    """
    # Make a mutable copy of elements
    elements = list(elements)
    n -= 1  # Convert to 0-indexed rank
    result = []

    for i in range(len(elements) - 1, -1, -1):
        f = math.factorial(i)
        index = n // f
        n %= f
        result.append(elements.pop(index))
    
    return result



digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 1_000_000

permutation = nth_lexicographic_permutation(digits, n)
permutation = ''.join(map(str, permutation))

print(f"The permutation is: {permutation}")

# Relative Links:
# https://en.wikipedia.org/wiki/Factorial_number_system
# https://en.wikipedia.org/wiki/Lehmer_code