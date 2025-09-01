
def double_dabble(bit_array):
    num_digits = int(len(bit_array) * 0.30103) + 2  # +2 for safety
    bcd = [0] * num_digits
    
    for bit in bit_array:
        # Add 3 to digits >= 5
        for i in range(len(bcd)):
            if bcd[i] >= 5:
                bcd[i] += 3
        
        # Shift left by 1
        carry = bit
        for i in reversed(range(len(bcd))):
            bcd[i] = (bcd[i] << 1) | carry
            carry = bcd[i] >> 4
            bcd[i] &= 0xF
    
    # Sum of decimal digits
    return sum(bcd)
    

# 2^1000
bits = [1] + [0] * 1000

sum_of_digits = double_dabble(bits)

print(sum_of_digits)
