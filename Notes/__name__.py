# waht is __name__ or __main__
print('this codes name is: ', __name__)

#every code is either run directly or 
#imported from another file
# the name of the func running directly is __main__
#if you import a lib while running it will be that name
# name of where code is running from is stores
# in var __name__
#__main__ is code ran directly

#if I import this to file named : "__importing__"
# run only the import line it will say __name__ = __name__ (this file)
# the import is running code from this file

# you can check if you are running directly:
def main():
	print ('this code is running from main')

if __name__ == '__main__':
	main()
else:
	print('runs from import')

	#on __improting__.py it wont go into the if
	#stetemnet because it isnt running from main
# if i want to run a method that is imported but ran only if __name__ = __main__
# I can use it on imported file using __name__.main() meaning file name . method in imported file
	