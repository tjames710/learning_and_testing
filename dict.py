# def packer(**kwargs):
# 	print(kwargs)

# def unpacker(first_name=None, last_name=None):
# 	if first_name and last_name:
# 		print("Hi {} {}!".format(first_name, last_name))
# 	else:
# 		print("Hi no name.")


# packer(name="Ted", num=42, dragon_age_inquisition=None)

# unpacker(**{"last_name": "Runyon", "first_name": "Ted"})


# template = "Hi, I'm {} and I love to eat {}!"

# values = [{"name": "Ted", "food": "Wopper"}, {"name": "James", "food": "Kiwi"}]

# def string_factory(values):
# 	return[template.format(**x) for x in values]

# print(string_factory())


# def word_count(s):
#     list_of_lowercase_words = s.lower().split() #Split the string at each space to seperate the words
#     dictionary_of_words = {} #Creating an empty dictionary
     
#     for word in list_of_lowercase_words:  #iterating through each word(entry) in l(our string that is split)
#         try:
#             dictionary_of_words[word] += 1 #Trying to create a key for each word in the string and counting how many times that word shows up in the string
#         except KeyError:
#             dictionary_of_words[word] = 1 #If error is thrown it will result in a value of 1

#     return dictionary_of_words #Returning the dictionary.

# print(word_count("I have a good sense of knowledge and a good amount of ambition"))


def num_teachers(teachers_courses): #Returns the number of teachers in the dictionary
	return(len(teachers_courses))


def num_courses(teachers_courses): #returns the total amount of courses in the dictionary
	return sum([len(courses) for courses in teachers_courses.values()])


def courses(teachers_courses):
	course_list = [] #Initializing an empty list
	for teacher in teachers_courses: #Iterating through the key values
		for courses in teachers_courses[teacher]: #Iterating through the value values
			course_list.append(courses) #adding each value from values to the list we created. 
	return course_list


def most_courses(teachers_courses):
	max_count = 0 #Initialize a counting variable.
	for teacher in teachers_courses: #Iterating through the dictionary
		if len(teachers_courses[teacher]) > max_count: #If the length of the key:value pair is greater than the max_count var
			max_count = len(teachers_courses[teacher]) #max_count will be assigned to the length.
			result = teacher
	return result #returning the result of which key has the longest value.
		
def stats(teachers_courses):
	teacher_course_list = [] #Initializing a new list
	for teacher, courses in teachers_courses.items(): #Iterating through the dictionary
		teacher_course_list.append([teacher, len(courses)]) #adding a list to our empty list
	return teacher_course_list




		# print("{} has {} courses.".format(teacher, len(teachers_courses[teacher])))
		







	# for teacher in teachers_courses:
		# print("{} has {} courses.".format(teacher, len(teachers_courses[teacher])))
			
		# return teacher, len(teachers_courses[teacher])
	
		
		

# print(num_teachers({"Ted Runyon": ["Python Formus", "Meetups", "Online"], "James": ["Python Professional", "Expert Python Coder"]}))

# print(num_courses({"Ted Runyon": ["Python Formus", "Meetups", "Online"], "James": ["Python Professional", "Expert Python Coder"]}))

# print(courses({"Ted Runyon": ["Python Formus", "Meetups", "Online"], "James": ["Python Professional", "Expert Python Coder"]}))

# print(most_courses({"Ted Runyon": ["Python Formus", "Meetups", "Online"], "James": ["Python Professional", "Expert Python Coder"]}))

print(stats({"Ted Runyon": ["Python Formus", "Meetups", "Online"], "James": ["Python Professional", "Expert Python Coder"]}))