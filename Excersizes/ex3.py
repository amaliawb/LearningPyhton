# excerise from internet https://pynative.com/python-functions-exercise-with-solutions/

# 1. function that can accept two arguments: name and age, a




#nd print its value -easy

def two_args(name, age):
    print(name, age)

two_args('amalia', 20)

# 2. Write a function func1() such that it can accept a variable
#    length of  argument and print all arguments value

def many_args(*args):
	if args:
		print(args)

many_args('amalia', 'is', 'cool')
# returns ('amalia', 'is', 'cool') creates tuple


def many_args2(*args):
	for i in args:
		print(i)

many_args2('amalia', 'is', 'cool')
# returns 
'''
amalia
is
cool
'''

# 3. Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. 
#    And also it must return both addition and subtraction in a single return call

def calculation(num1, num2):
    return num1+num2, num1-num2

ex3 = calculation(2,3)
print(ex3)

#also
def calculation(a, b):
    return a+b, a-b

add, sub = calculation(40, 10)
print(add)
print(sub)

# 4: Create a function showEmployee() in 
#such a way that it should accept employee 
#name, and it’s salary and display both, and if 
#the salary is missing 
#in function call it should show it as 9000

def showEmployee(required_name, salary = 9000):
	print('1. employee', required_name + '\'s', 'is:', salary)
	print(f'2. employee {required_name}\'s salary is: {salary}')

showEmployee('amalia')


