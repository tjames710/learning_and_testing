
# def squared(x):
#     try:
#         x = y = int(x) * x
#     except ValueError:
#         y = len(x) * x
#     print(y) 
    
# squared(5)
# squared("ted")




###################################################################
# You've seen how random.choice() works. It gets a random member from an iterable (like a list or a string).
# I want you to try and reproduce it yourself.
# First, import the random library.
# Then create a function named random_item that takes a single argument, an iterable. Then use random.randint() to get a random number between 0 and the length of the iterable, minus one. Return the iterable member that's at your random number's index.
# Check the file for an example.

# EXAMPLE
# random_item("Treehouse")
# The randomly selected number is 4.
# The return value would be "h"
#####################################################################
# import random

# def even_odd(num):
#     # If % 2 is 0, the number is even.
#     # Since 0 is falsey, we have to invert it with not.
#     return not num % 2

# start = 5

# while start > 0:
#     start -= 1
#     random_num = random.randint(1, 99)
#     if even_odd(random_num) != 0:
#         print("{} is even".format(random_num))
#     else:
#         print("{} is odd".format(random_num))


# my_list = [3, 5, 6, 7, 'ted', 'james']

# my_list.extend(['jen'])

# my_list.append('diesel')

# my_list.insert(1, 4)

# del my_list[4]

# print (my_list)

########################################################################
# This code takes a word and turns it into a list of characters,
# then it identifies if the char is a vowel and if it is, then we,
# take the vowel out and return the vowelless word.
# def disemvowel(word):
#     vowelless_word = list(word)

#     for char in word:
#         if char in 'aeiouAEIOU':
#             vowelless_word.remove(char)
            
#     return ''.join(vowelless_word)
    
# #######################################################################        
           
    

# print(disemvowel("apples"))

# print(disemvowel("crappes"))

# print(disemvowel("elephant"))

# print(disemvowel("iglou"))


# def first_4():
#     a = [4, 5, 6, 8, 9, 0, 12, 45]
#     first4_items = a[:4]
#     return first4_items

# def reverse_evens(a):
#     evens = a[::2]
#     reverse = evens[-1::-1]
    
#     return reverse
# print(reverse_evens([7, 8, 9, 3, 4, 6, 5, 123]))


##############################################################
# This function takes a string and makes the first half lower,
# case and the second half upper case.
def sillycase(s):
	length_by_2 = len(s) // 2
	s_list = list(s)
	first_half = s_list[:length_by_2]
	first = str.lower(''.join(first_half))
	second_half = s_list[length_by_2:]
	second = str.upper(''.join(second_half))
	return(first + second)

print(sillycase("happiest"))

###############################################################