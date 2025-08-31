def collatz_length(n, memo={}):
    if n == 1:
        return 0  # base case
    if n in memo:
        return memo[n]
    
    if n % 2 == 0:
        length = 1 + collatz_length(n // 2, memo)
    else:
        length = 1 + collatz_length(3 * n + 1, memo)
    
    memo[n] = length
    return length

def longest_collatz(limit):
    max_length = 0
    number_with_max_length = 1
    memo = {}
    
    for i in range(1, limit):
        length = collatz_length(i, memo)
        if length > max_length:
            max_length = length
            number_with_max_length = i
            
    return number_with_max_length, max_length


limit = 1_000_000

number, length = longest_collatz(limit)

print(f"The number under {limit} with the longest Collatz sequence is {number} with length {length}.")

