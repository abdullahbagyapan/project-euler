
import math

def index_by_digits(target_digits: int) -> int:
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    return math.ceil(((target_digits - 1) + math.log10(sqrt5)) / math.log10(phi))


target_digits = 1000

index = index_by_digits(target_digits)

print(f"The index is: {index}")

# Relative Links:
# https://en.wikipedia.org/wiki/Fibonacci_sequence
# https://en.wikipedia.org/wiki/Binet_equation
