# methods and string manipulation
# can call everything also with str.method(strliteral)


message = 'hello10'
print(message.isalpha())

print(message.isalnum())

#  RANGE()
range(6)  # => [0, 1, 2, 3, 4, 5]
range(1, 6)  # => [1, 2, 3, 4, 5]
range(1, 6, 3)  # => [1, 4]
'''
range(stop)
range(start, stop)
range(start, stop, step)
'''

# .isalpha --- check if all letters in string are letters - no whitespace
message = 'hello'
print('is hello alpha:', message.isalpha())
message = 'hello world'
print('is hello world alpha:', message.isalpha())

# .isalnum - all are either alpha or num - no whitespaces
message = 'hello10'
print('is hello alnum:', message.isalnum())
message = 'hello world 10'
print('is hello world alnum:', message.isalpha())

# .isdecimal ,,, .isnumeric ,,, .isdigit

# reverse a string
message = 'Hello world'
print(message[::-1])

# LOWER/UPPER CASE method
print(message.lower())  # running lower methos on the string
print(message.upper())  # same

# COUNT method - counts number of times the word passed as arg repeats in str 
print(message.count('Hello'))
print(message.count('l'))

# FIND method- finds the index of the first letter of str i want to find
print(message.find('world'))
print(message.find('l'))
# will print -1 means no

# REPLACE method -
message = ('Hi , I am Amalia')
print(message)
new_message = message.replace('I am',
                              'my name is')  # need to set new var to get return value, cant just replace and print message. does not change messgae, sets new return value to new var

# SPLIT method
message1 = 'hi my name amalia'
print(message1.split())
print(message1.split("a"))  # splits at every a and removes it
print(message1.split("a", 1))  # splits only at first a

# JOIN
# "string that goes between every item of list".join(list)
list1 = ['hi', 'there', 'you']
list2 = ['whatcha', 'doin', '?']

print(' '.join(list1))
print(' '.join(list1))

print(new_message)
# to change message u need to set var again
message = message.replace('I am', 'my name is')
print(message)

# concatinate strings together
greeting = 'hello'
name = 'amalia'
message = greeting + ', ' + name + '. welcome'  # need to add space
print(message)

# FORMAT
# method - formatted string to make vars readable
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)
# in py 2 fomatting is done with % insteaed of {} an no method
# %s for strings %d for decimals and %0X nums from 0 to 2 places after
# print('Hello my name %s i am %s old') % (amalia, 20)

# F'STRING
# from py 3.6 and above - make str formatting easy
message = f'{greeting}, {name}. WELCOME'
print(message)

# ENUMARATE
# returns method adds counter to an iterable and returns it. The returned object is a enumerate object.
# You can convert enumerate objects to list and tuple using list() and tuple() method respectively.

list3 = ['one', 'two', 'three']

for i, j in enumerate(list3):
    print(i, j)

print(list(enumerate(list3)))

# ZIP
# zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
# zip can handle three or more lists as well!

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    print(max(a, b))

# MAP
# map(function, iterable) maps the function on each item of the iterable (like for loop)

rang = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def double(x):
    return x * 2


rang2 = []

for i in rang:
    rang2.append(i * 2)

print('\nMAP:::\nthis is appending from loop1 to print loop2 with for loop:', rang2)

print('this is using map on loop2 with double as func:', list(map(double, rang2)))

# LIST COMPREHENSION
print('---list comprehension pythonic way of coding\nrang is:', rang)
doubled = [x * 2 for x in rang]
print('this is doubled rang: ', doubled)


# FILTER
# filter(functionT/F, iterable)
# uses function that returns True or False to filter iterables and return only item that are true by the funxtion

def is_even(x):
    return x % 2 == 0
    # if ==0 it will return true


print('\nFILTER::\n')
print('filtered rang with even', list(filter(is_even, rang)))
# LIST COMPREHENSION
print('---pythonic way of coding\n')
evens = [x for x in rang if x % 2 == 0]
print('with onle line for loop:', evens)

# REDUCE
# IMPORTED
from functools import reduce

# reduce(functiontoreduce, iterable)
blist = [1, 2, 3, 4, 5]
clist = []


def sum(x, y):
    return x + y


print('\nREDUCE:\n', blist)
print(reduce(sum, blist))
# reduce takes element 1 and 2, uses sum on them, and then uses the returned value as element 1 ant takes element 3 as element2

# WHAT IF THE LIST IS EMPTY????
print('if the list is empty - reduce wont be able to use sum on it')
# add initial condition 0 to the sum and if list is empty it will be 0
print('add initial condition reduce(func, iterable, condition 0)')
print(reduce(sum, clist, 0))
