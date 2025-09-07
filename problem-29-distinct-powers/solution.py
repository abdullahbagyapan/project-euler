
def number_spiral_diagonals(n):
    total = 1  # center value
    for size in range(3, n + 1, 2):  # odd sizes only
        total += 4 * size * size - 6 * (size - 1)
    return total

print(number_spiral_diagonals(1001)) # 669171001
