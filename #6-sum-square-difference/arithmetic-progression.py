
def sum_of_squares(N):
    
    sum = (N * (N + 1) * ((2*N) + 1)) / 6
    return sum

def square_of_sums(N):
    
    sum = ((N * (N + 1)) / 2)**2
    return sum



N = 100

sum_of_square = sum_of_squares(N)
square_of_sum = square_of_sums(N)

sum_square_difference = square_of_sum - sum_of_square


print(f"Sum Square Difference is : {sum_square_difference}")   # Output should be 25164150


# Relative links:
# https://en.wikipedia.org/wiki/Arithmetic_progression
