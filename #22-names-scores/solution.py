
def get_names(filename="names.txt"):

    file = open(filename, "r")
    content = file.read()
    file.close()

    names = content.replace('"', '').split(",")

    return names

def alphabet_sum(s):
    
    total = 0

    for char in s:
        total += ord(char) - ord('A') + 1

    return total

def names_scores(names):

    total = 0

    names = sorted(names)

    for i, name in enumerate(names, start=1):

        alphabetic_sum = alphabet_sum(name)

        total += i * alphabetic_sum

    return total



names = get_names()

total = names_scores(names)

print(f"The total of all the name scores is: {total}") # 871198282