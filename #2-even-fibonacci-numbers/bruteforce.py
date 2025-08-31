# even + even = even 
# odd + odd = even   
# even + odd = odd   

# Sequence: odd(1) - even(2) - odd(3) - odd(5) - even(8) - odd(13) - odd(21) - even(34) ...

sum = 0

i = 1 # F(1)
j = 2 # F(2)


while (j < 4000000) :

    if (j % 2 == 0):
        sum += j

    # next iteration
    k = i + j
    
    i = j
    j = k

print(sum) # Output should be 4613732


# Relative links:
# https://en.wikipedia.org/wiki/Fibonacci_sequence