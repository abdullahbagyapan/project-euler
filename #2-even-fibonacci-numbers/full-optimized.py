# even + even = even 
# odd + odd = even   
# even + odd = odd   

# Sequence: odd(1) - even(2) - odd(3) - odd(5) - even(8) - odd(13) - odd(21) - even(34) ...

# Even number sequence is: even(n) = 4 * even(n-1) + even(n-2)
# The only difference from ``mid-optimized.py` is we dont compute odd numbers

sum = 0

# first two even fibonacci number
i = 2
j = 8

sum += i

while (j < 4000000):
    
    sum += j
    
    # next iteration
    k = (4 * j) + i
    
    i = j
    j = k
    
print(sum) # Output should be 4613732


# Relative links:
# https://en.wikipedia.org/wiki/Fibonacci_sequence