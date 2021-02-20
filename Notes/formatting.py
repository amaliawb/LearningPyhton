# formatting
name = 'Amalia'

# .format - string formatting
# 'somthing{}'.format(what is in {})
print('reg .format:')
print('hello my name is {}'.format(name))
print()

# fstring
print('fstrings:')
print(f'hello my name {name}')
print()

# % - formatting with ints
# %d decimal %s string %1.5f float
#                  1 nums before decimal place. 5 nums after decimal place
# printing %s with (int 5) will work cause it converts the int into str. wont work when there is also a string to format into and it doesnt know where to put it
print('int+str formatting:')
print('hello I am called %s' % (name))
print()

# unpacking lists and dict
print('unpacking list and strings into format:')
list1 = [1, 2, 3, 4]
song = '{}, {}, {}, {}, can I have a little more'.format(*list1)
# or specify
song = '{0}, {1}, {2}, {3}, can I have a little more'.format(*list1)
print(song)

beatles = {
    'names': 'johnpaulgeorgeringo',
    'loved': 'john and paul'
}
message = 'the beatles names are {names}.\nBut the only ones that matter are {loved}\n'.format(**beatles)
print(message)

# : in {} specifies we want the data formatted too
print('formatting {} with {:?}')
# allows number to be printed: start with 0 if not padded, and have 2 digit
print()
print('padding int with 0:')
for i in range(1, 11):
    print('the value is: {:02}'.format(i))

# specify decimal places .xx
print('\nspecify decimal places after float:')
pi = 3.14159
print('pi is = to {:.2f}'.format(pi))
print()

# comma formatted nums
print('comma formatting:')
print('this is a large num: {:,}\n'.format(1000 ** 2))

# formatting dates
print('formatting datetime:')
import datetime

my_date = datetime.datetime(2021, 2, 20, 10, 24)  # stores said date
print(my_date)

sentence = '{:%B %dth, %Y}'.format(my_date)  # formatting with %CHR from the datetime library python docs
print(sentence)

sentence_big = '{0:%B %dth, %Y} fell on a {0:%A}'.format(my_date) # need to add 0 index of mydate becayuse it isnt passing several args; it is passing one arg with multiple meanings?
print(sentence_big)
