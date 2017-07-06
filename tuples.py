# def multiply(*args): #(*args) packs a tuple with the values given in the argument at calling. 
# 	product = 1 #Product or total intitialized. If adding or subtracting should set to zero.
# 	for a in args: #Here I'm looping through each value given to the args argument.
# 		product *= a #Here I'm multipling each value.
# 	return product #And finally returning the value.
# #What is so neat about this is that you can virtually have as many arguments as you want.

# print(multiply(2, 4))


# #Created a dictionary and when looped through gives back a tuple. 
# course_minutes = {"Python": 232, "Java": 322, "C#": 421, "PHP": 145}

# for course, minutes in course_minutes.items():
# 	print("{} is {} minutes long.".format(course, minutes))

#===============================================================|
# list(enumerate("abc"))

# for index, letter in enumerate("abcedfghijklmnopqrstuvwxyz"):
# 	print("{}: {}".format(index + 1, letter))

#===============================================================|
'''Here I have a function that will take any string and return,
that string in upper case, lower case, title case and reversed!'''
# def stringcases(*args):
# 	for a in args:
# 		result = a.upper(), a.lower(), a.title(), a[::-1]
# 	return result


# print(stringcases("hello there i am ted."))

#==============================================================|

'''This function takes two iterable items and creates a list of tuples,
with the first tuple being the first item in each iterable, then the second set,
and so on.'''
def combo(l, s):
	result = []
	for i in range(0, len(l)):
		result += (l[i], s[i]),
	return result
		

print(combo([1, 2, 3], 'abc'))