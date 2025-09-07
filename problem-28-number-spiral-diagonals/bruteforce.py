
def distinct_powers(lower_limit, upper_limit):

    terms = set()

    for a in range(lower_limit, upper_limit + 1):

        for b in range(lower_limit, upper_limit + 1):
            
            term = pow(a,b)

            terms.add(term)

    return len(terms)



lower_limit = 2
upper_limit = 100

length = distinct_powers(lower_limit, upper_limit)

print(f"The distinct power number is {length}") # Output should be 9183