
def get_upper_limit(n):
    k = 1
    while k * (9 ** n) >= 10 ** (k - 1):
        k += 1
    return (k - 1) * (9 ** n)

def get_digits(n):

    digits = [int(d) for d in str(n)]

    return digits

def sum_of_digit_n_powers(limit, n):

    total = 0

    pow_table = [d ** n for d in range(10)]

    for i in range(2, limit):

        digits = get_digits(i)

        sum_of_n_powers = 0

        for d in digits:

            sum_of_n_powers += pow_table[d]

            if sum_of_n_powers > i:
                break

        if (sum_of_n_powers == i):
            total += sum_of_n_powers

    return total



n = 5
limit = get_upper_limit(n)

total = sum_of_digit_n_powers(limit, n)

print(f"The sum of digit {n} powers is: {total}")