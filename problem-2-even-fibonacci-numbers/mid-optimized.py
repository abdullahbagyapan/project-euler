# even + even = even 
# odd + odd = even   
# even + odd = odd   

# Every third number is even: F(2) - F(5) - F(8)...
# Sequence: odd(1) - even(2) - odd(3) - odd(5) - even(8) - odd(13) - odd(21) - even(34) ...
even_sequence_number = 3
sequence_iterator = 0

sum = 0

i = 1
j = 2

sum += j

while (j < 4000000) :
     
    # get every 3th iteration 
    if (sequence_iterator == even_sequence_number):
        sequence_iterator = 0
        sum += j
    
    # next iteration
    k = i + j
    
    i = j
    j = k
    
    sequence_iterator += 1

print(sum) # Output should be 4613732


# Relative links:
# https://en.wikipedia.org/wiki/Fibonacci_sequence