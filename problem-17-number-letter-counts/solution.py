
def count_number_letters():

    letters_counts_ones = (3,3,5,4,4,3,5,5,4)                   # 1 to 9
    letters_counts_ten = (3)                                    # 10
    letters_counts_teens  = (6,6,8,8,7,7,9,8,8)                 # 11 to 19
    letters_counts_tens = (6,6,5,5,5,7,6,6)                     # 20 to 90
    letters_counts_hundreds = (7,10)                            # 100, hundred and
    letters_counts_thousands = (11)                             # 1000


    # from 1 to 99
    n1_to_n99 = (sum(letters_counts_ones)*9) + letters_counts_ten + sum(letters_counts_teens) + (sum(letters_counts_tens)*10)

    # from 100 to 900
    n100_to_n999 = (sum(letters_counts_ones)*100 + letters_counts_hundreds[0]*9) + (letters_counts_hundreds[1]*99)*9 + n1_to_n99*9

    # 1000
    n1000 = letters_counts_thousands
    
    letters_count = n1_to_n99 + n100_to_n999 + n1000

    return letters_count
    
    
number_letters_sum = count_number_letters()


print(number_letters_sum)    # 21124 

