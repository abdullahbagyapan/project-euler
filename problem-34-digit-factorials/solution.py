import math

def get_digits(n):
    digits = []
    
    while n > 0:
        digit = n % 10
        n //= 10
        
        digits.append(digit)
    
    return digits


def digit_factorials(lower_limit, upper_limit, factorials):
    
    curious_numbers = []
    
    for i in range(lower_limit, upper_limit+1):
        
        digits = get_digits(i)
        
        factorial_of_digits = [factorials[i] for i in digits]
        
        sum_of_factorials = sum(factorial_of_digits)
        
        if (sum_of_factorials == i):
            curious_numbers.append(i)
    
    return curious_numbers



factorials = [math.factorial(x) for x in range(0,10)]

upper_limit = 2_540_160 # 7x9!
lower_limit = 10

curious_numbers = digit_factorials(lower_limit, upper_limit, factorials)

print(curious_numbers)    
print(sum(curious_numbers))