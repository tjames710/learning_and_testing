def multiply(*args): #(*args) packs a tuple with the values given in the argument at calling. 
	product = 1 #Product or total intitialized. If adding or subtracting should set to zero.
	for a in args: #Here I'm looping through each value given to the args argument.
		product *= a #Here I'm multipling each value.
	return product #And finally returning the value.
#What is so neat about this is that you can virtually have as many arguments as you want.

print(multiply(2, 4))


