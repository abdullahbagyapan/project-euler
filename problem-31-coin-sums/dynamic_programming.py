
def coin_sums(coins, target):
    
    ways = [0] * (target + 1)
    ways[0] = 1  # Base case: one way to make 0p (no coins)

    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]

sum_of_ways = coin_sums(coins, target)

print(f"Number of ways: {sum_of_ways}") # The output should be 73682
