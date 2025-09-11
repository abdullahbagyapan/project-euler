from fractions import Fraction

def algebraic_digit_cancelling():
    product = Fraction(1, 1)
    solutions = []

    # Digits are 1-9 (avoid zeros to skip trivial fractions)
    digits = range(1, 10)

    # Case 1: tens-tens cancelled: a=c, fraction = b/d
    for a in digits:
        for b in digits:
            for d in digits:
                if b == d:
                    continue  # trivial cancellation
                numerator = 10*a + b
                denominator = 10*a + d
                if numerator < denominator and Fraction(numerator, denominator) == Fraction(b, d):
                    solutions.append((numerator, denominator))
                    product *= Fraction(numerator, denominator)

    # Case 2: tens-units cancelled: a=d, fraction = b/c
    for a in digits:
        for b in digits:
            for c in digits:
                numerator = 10*a + b
                denominator = 10*c + a
                if numerator < denominator and Fraction(numerator, denominator) == Fraction(b, c):
                    solutions.append((numerator, denominator))
                    product *= Fraction(numerator, denominator)

    # Case 3: units-tens cancelled: b=c, fraction = a/d
    for b in digits:
        for a in digits:
            for d in digits:
                numerator = 10*a + b
                denominator = 10*b + d
                if numerator < denominator and Fraction(numerator, denominator) == Fraction(a, d):
                    solutions.append((numerator, denominator))
                    product *= Fraction(numerator, denominator)

    # Case 4: units-units cancelled: b=d, fraction = a/c
    for b in digits:
        for a in digits:
            for c in digits:
                numerator = 10*a + b
                denominator = 10*c + b
                if numerator < denominator and Fraction(numerator, denominator) == Fraction(a, c):
                    solutions.append((numerator, denominator))
                    product *= Fraction(numerator, denominator)

    return solutions, product

# Solve
solutions, product = algebraic_digit_cancelling()

print("Curious fractions found:")
for n, d in solutions:
    print(f"{n}/{d}")

print("\nProduct in lowest terms:", product)
print("Denominator:", product.denominator)
