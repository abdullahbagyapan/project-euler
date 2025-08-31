from math import gcd

def pythagorean_triples_with_sum(S):

    D = S // 2
    triples = []

    for m in range(1, int(D**0.5)+1):

        if D % m == 0:
            M = D // m

            for k in range(1, M//m + 1):

                if (M // k) * k != M:
                    continue

                n = (M // k) - m

                if n > 0 and m > n and gcd(m, n) == 1 and (m - n) % 2 == 1:
                    a = k * (m**2 - n**2)
                    b = k * (2 * m * n)
                    c = k * (m**2 + n**2)
                    triples.append(tuple(sorted((a,b,c))))

    return triples


S = 1000

triples = pythagorean_triples_with_sum(1000)

for triple in triples:
    print("Product abc =", triple[0] * triple[1] * triple[2])       # Output should be 31875000


# Relative Links:
# https://en.wikipedia.org/wiki/Pythagorean_triple
# https://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples