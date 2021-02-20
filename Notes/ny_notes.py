# my notes
'''
- doesnt need ;
can use " and ' in print string and \' \" to print the signs
can use escape char \*
function = 
method = function that belongs to an object object.method
return 0 means successfully executed.
return 1 means executed but some error may have occured

'''

# comment
'''
multipleline commet
'''

'''
IMPORTANT NOTES

- to check if there is input
if len(variable) > 0:
    do somthing with it
else:
    print empthy or return 1?

- method.isalpha() checks if the string is only chars

- seder peulot - 1111 not 2222 and 3333 or 444 is not/not in

- *args **kwargs - key word arguments
  

'''

# concatanation:
print("hi" + "there")  # will print hithere, no space unless i put one in ""
print("hi", "there")  # will put space in between

# strings and integer conversion
print("hi" + str(5))  #

# print('8' + 5) # cant do it 8 isnt int
print(int('8') + 5)  # can do with float

# math operation


# unpacking - unpacks x into x and y into y
x, y = (3, 5)
print(x)
print(y)

# multi line string
message = """This will print the text
in multiple lines like i am writing now"""
print(message)

# length of string
print(len(message))

# index of string char printing
print(message[0])
# IndexError will be thrown back if i try to print an index that doesnt exist.

# slicing::: print part of a string from 0 to the 5th - last index is not included!!
print(message[0:6])
print(message[:6])  # not specifying start index will print from i = 0
print(message[6:])  # not specifting end i will print from i = 6 to the end of str


def not_string(str):  # makes str with not infront
    if len(str) >= 3 and str[:3] == 'not':
        return str
    else:
        new_str = 'not ' + str
        return new_str


# LOWER/UPPER CASE method
print(message.lower())  # running lower methos on the string
print(message.upper())  # same

# COUNT method - counts number of times the word passed as arg repeats in str 
print(message.count('multiple'))
print(message.count('m'))

# FIND method- finds the index of the first letter of str i want to find
print(message.find('print'))
print(message.find('amalia'))
# will print -1 means no

# REPLACE method -
message = ('Hi , I am Amalia')
print(message)
new_message = message.replace('I am',
                              'my name is')  # need to set new var to get return value, cant just replace and print message. does not change messgae, sets new return value to new var
print(new_message)
# to change message u need to set var again
message = message.replace('I am', 'my name is')
print(message)

# concatinate strings together
greeting = 'hello'
name = 'amalia'
message = greeting + ', ' + name + '. welcome'  # need to add space
print(message)

# FORMAT method - formatted string to make vars readable
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)
# in py 2 fomatting is done with % insteaed of {} an no method
# %s for strings %d for decimals and %0X nums from 0 to 2 places after
# print('Hello my name %s i am %s old') % (amalia, 20)

# fstrings - from py 3.6 and above - make str formatting easy
message = f'{greeting}, {name}. WELCOME'
print(message)

# knowledge on pyhton functions and methods

# DIR function - if you pass in a var to the dir function it will show all methods i can use on that var
print(dir(name))

# HELP function
print(help(str))  # runs help on all string class everything u can do on string
print(help(len))

# MATH
remainder = 15 % 2  # 14/2 +1
print(remainder)

num = 7. / 2  # in py 2 division of int returns int not float. turn int to float with . after one of the nums in division
num = float(7) / 2
print(num)

# IMPORTING datetime library
from datetime import datetime

now = datetime.now()
print(now)
print(now.year)  # specific data in datetime.now
print(now.month)
print(now.day)

''' with formatting in py 2 - TRY WITH PY 3 FORMATTING why d is int but in str
from datetime import datetime
now = datetime.now()
print('%02d/%02d/%04d') % (now.month, now.day, now.year)

print '%02d:%02d:%04d' % (now.hour, now.minute, now.second)

'''

# IF statement ELSE
# assignamet statement
'''
<=
>=
!=
== som equals to som
'''
x = 5
y = 8
z = 5

if x > y:
    print('x is graeter than y')
if x < y:
    print('x is less than y')

if x < y > x:
    print('y is graeeter than z and x')

else:
    print('no')

# somthing else ; else applies to the last if

amalia = 20
ruth = 17
elah = 48

if amalia > elah:
    print('amalia is older than elah')

if amalia > ruth:
    print('amalia older than ruth')

else:
    print('amalia not older than ruth')

# to tie together all ifs : ELIF

if amalia > elah:
    print('amalia is older than elah')
elif amalia > ruth:
    print('amalia older than ruth')
elif elah > amalia:
    print('elah older amalia - not gonna print cuz amalia older than ruth')
else:
    print('if and elif never ran')


# FUNCTIONS
# define
# function name and in () the parameters
def example():
    print('\nbasic function learning')
    a = 2 + 6
    print(a)


example()


# or call the function in terminal without calling it in code

# PARAMETERS for functions
def simple_addition(num1, num2):
    answer = num1 + num2
    print('\nnum1 is', num1, 'num2 is', num2)
    print(answer)
    # when calling function I specify the parameters


simple_addition(2, 5)
simple_addition(num2=3, num1=6)  # explicit parameter specification


# DEFAULT FUN PARAMETERS

def simple(num1, num2):
    pass


# when parameter is specified in fun define u dont have to specify it when calling, it is always that

def simple(num1, num2=5):
    print(num1, num2)


simple(3)


# use when creting windows --- bgc backgtound colour TNR times new roman
def basic_window(width, height, font='TNR', bgc='w', scrollbar=True):
    print(width, height, font, bgc)


basic_window(500, 350, 'a')

basic_window(500, 350, bgc='w')
# specify name when u want to change parameters


# GLOBAL var and LOCAL var
# var reach within program
# GLOBAL = var that can be accessed anywhere
# LOCAL - var that can be accessed only within its frame/program/function

x = 6  # not global,


def example2():
    z = 5
    print(z)
    print(x)  # will access x because its before the fun in program

    '''x+=6'''  # redefinition of var will not work because x not global to the function


example2()


def example3():
    global x
    print('this is global x', x)
    x += 5
    print('redefintioin of global x', x)


example3()

# ways arounsd using globals - to not redifine a global var

a = 10  # not a global, will throw error if redfined in function ex4


def example4():
    globa = a  # local to function i named var and set it to var outside function to use in the function
    print('now a is global in this function:', globa)
    globa += 5
    print('redefinition of a as global is this function', globa)
    print('but a is still local', a, 'outside this function')


example4()


def example5():
    globa = a  # local to function i named var and set it to var outside function to use in the function
    print('\n\nnow a is global in this function:', globa)
    globa += 10
    print('redefinition of a as global is this function', globa)
    print('but a is still local', a, 'outside this function')

    print('return')

    return globa


a = example5()
print(a)  # modifying a outside function without using it globals


# RETURN TYPES

def double_it(x):
    return 2 * x  # the function becomes the return value wherever its called
    # when u use return u can print the value that the fun becomes


x = double_it(4)
print('\nthe function = x now which is:', x)

print('i am now printing the function intself:', double_it(5))


# use functions with ifs and returns

def function1(num):
    if num > 5:
        return "bigger"
    elif num < 5:
        return "smaller"
    else:
        return "it is equal to!"


print(function1(5))
print(function1(8))

# MODULES -
'''
random module
when u import a module all functions from it are methods?
if i want to use randint method from random module i will: random.randint(min,max)
'''
