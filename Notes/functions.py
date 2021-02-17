#FUNCTIONS

'''
- *args **kwags
	- returns extra arguments in tuples, and extra key word args in dictionaries
	- extra arguments and keyword arguments
	- positional arguments = args based on position in func call
	- keyword args = keyword = value, when theres an arg in calling a func which has a var set to 
 	 it meaning that if specified it doesnt matter in which position in the calling

- if func() returns an str u can use
string methods on it like func().lower
'''


def func(required_arg, *args, **kwargs):
	print(required_arg)
	if args:
		print(args)
	if kwargs:
		print(kwargs)


    #define
    # function name and in () the parameters
def example():
    print('\nbasic function learning')
    a = 2 + 6
    print(a)

example()

    #or call the function in terminal without calling it in code

 #PARAMETERS for functions
def simple_addition(num1,num2):
    answer = num1 + num2
    print('\nnum1 is', num1, 'num2 is', num2)
    print(answer)
    # when calling function I specify the parameters

simple_addition(2,5)
simple_addition(num2 = 3, num1 = 6) #explicit parameter specification

#DEFAULT FUN PARAMETERS

def simple(num1,num2):
    pass


#DEFAULT VALUE IN FUNC = when parameter is specified in fun define u dont have to specify it when calling, it is always that

def simple(num1, num2 = 5):
    print(num1,num2)

simple(3)


## calling functions in functions
def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2

  #more and % division if number is divisible ny 3

def cube(number):
  return number*number*number

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else: 
    return False


# abs type 
def distance_from_zero(x):
  if (type(x) == int or type(x) == float):
    return abs(x)
  else:
    return 'Nope'
