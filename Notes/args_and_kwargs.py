#args and kwargs

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

student_info('math', 'art', name = 'john', age = 20)
# returns a tuple with the *args positional args 
# and a dictionary with **kwargs key word args

courses = ['geometry', 'physics']
info = {'name':'amalia', 'age':20}

student_info(courses,info) 
#returns a tuple with the list and dict as the args 
#because i didnt set key words to them

student_info(*courses, **info)
#unpacks list and dict 