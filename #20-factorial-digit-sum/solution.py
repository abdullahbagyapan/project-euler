import math

factorial = math.factorial(100)

digits = str(factorial)

digit_sum = sum(int(digit) for digit in digits)

print(f"The sum of digits is: {digit_sum}")

