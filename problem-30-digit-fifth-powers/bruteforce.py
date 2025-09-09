
def get_upper_limit(n):
    k = 1
    while k * (9 ** n) >= 10 ** (k - 1):
        k += 1
    return (k - 1) * (9 ** n)


def get_digits(n):

    digits = [int(d) for d in str(n)]

    return digits

def sum_of_digit_n_powers(n, limit):

    total = 0

    for i in range(2, limit):

        digits = get_digits(i)

        sum_of_n_powers = sum(d**n for d in digits)

        if (sum_of_n_powers == i):
            total += sum_of_n_powers

    return total



n = 5
limit = get_upper_limit(n)

total = sum_of_digit_n_powers(limit, n)

print(f"The sum of digit {n} powers is: {total}")