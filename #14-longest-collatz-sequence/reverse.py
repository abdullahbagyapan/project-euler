def collatz_reverse(n):
    
    sequence = []
    
    collatz_even = 2*n
    sequence.append(collatz_even)
    
    if ((n-1) % 3 == 0):
        
        collatz_odd = (n-1) // 3
        sequence.append(collatz_odd)
        
    return sequence
    
def collatz_forward(n,cache):
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1
    cache[n] = 1 + collatz_forward(next_n, cache)
    return cache[n]
    

def longest_collatz_sequence(limit):
    
    sequence = {}
    sequence[1] = 1
    
    for i in range(1, limit + 1):
        
        if (i in sequence):
            reverse_sequences = collatz_reverse(i)
        
            for reverse_collatz in reverse_sequences:
                
                if (reverse_collatz in sequence):
                    continue
                else:
                    sequence[reverse_collatz] = sequence[i] + 1
                
            continue
        else:
            collatz_forward(i, sequence)
        
    # Get the key with the max value
    max_key = max(sequence, key=sequence.get)
    
    # Get the max value
    max_value = sequence[max_key]
    
    print(f"Key: {max_key}, Value: {max_value}")

    

limit = 1_000_000

longest_collatz_sequence(limit)