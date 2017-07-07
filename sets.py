''' Here I created a set, then added an item to the set and then used the,
update method to add two more sets to my songs set. '''

# songs = {"Salvation", "Unforgiven", "Where ever I may roam"}
# songs.add("Treehouse Hula")
# songs.update({"Python Two-Step", "Ruby Rhumba"}, {"My PDF Files"})

# print(songs)

#====================================================================|

# COURSES = {
#     "Python Basics": {"Python", "functions", "variables",
#                       "booleans", "integers", "floats",
#                       "arrays", "strings", "exceptions",
#                       "conditions", "input", "loops"},
#     "Java Basics": {"Java", "strings", "variables",
#                     "input", "exceptions", "integers",
#                     "booleans", "loops"},
#     "PHP Basics": {"PHP", "variables", "conditions",
#                    "integers", "floats", "strings",
#                    "booleans", "HTML"},
#     "Ruby Basics": {"Ruby", "strings", "floats",
#                     "integers", "conditions",
#                     "functions", "input"}
# }

# def covers(topics):
# 	course_list = []
# 	for course_name, course_value in COURSES.items():
# 		if course_value & topics:
# 			course_list.append(course_name)
# 	return course_list

# print(covers({"Java"}))


''' These next two functions do the same thing but look a little different,
the first function is what I came up with it is very similar to the function,
above, I guess for learning purposes it's alright. '''

# def covers_all(s):
# 	courses = []
# 	for course_name, course_topics in COURSES.items():
# 		if course_topics & s:
# 			courses.append(course_name)
# 	return courses

# def covers_all(s):
# 	courses = []
# 	for course in COURSES:
# 		if s.issubset(COURSES[course]):
# 			courses.append(course)
# 	return courses

# print(covers_all({"input"}))
