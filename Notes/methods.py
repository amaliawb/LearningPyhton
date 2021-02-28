# methods and string manipulation
# can call everything also with str.method(strliteral)


message = 'hello10'
print(message.isalpha())

print(message.isalnum())

#  RANGE()
range(6) # => [0, 1, 2, 3, 4, 5]
range(1, 6) # => [1, 2, 3, 4, 5]
range(1, 6, 3) # => [1, 4]
'''
range(stop)
range(start, stop)
range(start, stop, step)
'''

# .isalpha --- check if all letters in string are letters - no whitespace
message = 'hello'
print('is hello alpha:',message.isalpha())
message = 'hello world'
print('is hello world alpha:',message.isalpha())

# .isalnum - all are either alpha or num - no whitespaces
message = 'hello10'
print('is hello alnum:',message.isalnum())
message = 'hello world 10'
print('is hello world alnum:',message.isalpha())

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

# FORMAT method - formatted string to make vars readable
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)
# in py 2 fomatting is done with % insteaed of {} an no method
# %s for strings %d for decimals and %0X nums from 0 to 2 places after
# print('Hello my name %s i am %s old') % (amalia, 20)

# fstrings - from py 3.6 and above - make str formatting easy
message = f'{greeting}, {name}. WELCOME'
print(message)
