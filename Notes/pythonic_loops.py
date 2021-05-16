# PYTHONIC LOOPS

# writing for loop in one line and assigning the result of the loop into a list
from typing import Optional, List

dlist = ['a', 'b', 'c']

# my_list =
# [do this FOR each this IN this]
print([index * char for index, char in enumerate(dlist)])

# print(my_list)

print('\ndict items into tuple for loop:')

my_dict = {1: 11, 2: 22, 3: 33}

print([my_tup for my_tup in my_dict.items()])
# my_dict.items returns a list of tuples in which the key and value are the elements.
# weird syntax

multiple_keyvalue = [key * value for (key, value) in my_dict.items()]
# multiplies key and val in the list of tuples that dict.items makes

print(multiple_keyvalue)

# joining lists?

nums_in_str = ['one', 'two', 'three', 'four']
nums_in_int = [1, 2, 3, 4]

print('\n')
print('this is the list the zip 2 lists creates: ', list(zip(nums_in_int, nums_in_str)))
print('\n')

# one line to print each corresponding indexes
[print(f'{string} corresponds to {integer}') for (string, integer) in zip(nums_in_str, nums_in_int)]

# creating dict out of two list:
dict_nums = dict(zip(nums_in_int, nums_in_str))
print(dict_nums)

[print(f'{key1} corresponds 2 {value2} ') for (key1, value2) in dict_nums.items()]

# pythonic ifs
# print('a is 1') if a==1 else ('a is 7') --- on idle it works
# you must end with else otherwise you cant o it one line
# TO THE IF MUST BE ONLY ONE OUTCOME NOT TWO THINGS THAT HAPPEND INSIDE THE IF
# 4EXAMPLE = YOU CANT ASSIGN A IS FIVE TO THING_TO_PRINT AND ALSO CHANGE A ASSIGNAMENT TO 7. ONLY CHANGE ONE THING


print('\npythonic ifs: >>>>>>>>>')
a = 7

print('a is 1') if a == 1 else print('1) a = 7')  # --- works here with no assignament

yes = ('a is 1') if a == 1 else ('2) a is 7')
# written regularly:
'''
if a == 1:
    yes = ('a is 1')
else:
    yes = ('a is 7')
'''
print(yes)

# else if

a = 10

thing_to_print = '3) a is five' if a == 5 else 'a is nine' if a == 9 else '3) a is something else'
print(thing_to_print)

# with loops -
# you can put if one line in for one line and you dont need else in that case

my_list = [ele for ele in [1, None, 2, 3, None, 4] if ele != None]  # no need to end with else if starts with for
# ele will be in the list FOR every ele IN the list IF it is not == none
print(my_list)

# making dict for loop - 2 lists

list1 = [1, 2, 3, 4]
list2 = ['one', 'two', 'three', 'four']

dict12 = {list1[x]: list2[x] for x in range(len(list2)) if x != 4}
#         put key:value for every index in range of the length of list but dont go in the loop if x is 4
print(dict12)

# create a list that multiplies 1 through 9 by 100 only in the number 1-9 is even

one2nine = [1, 2, 3, 4, 5, 6, 7, 8, 9]

first_list = [ele * 100 for ele in one2nine if ele % 2 == 0]
print(first_list)

# if there is a remainder put the original number in the list
# DO IN LOOP if this else DO INFORLOOP for ....
second_list = [(ele * 100) if ele % 2 == 0 else ele for ele in one2nine]
print(second_list)

# 7 boom
numbers = range(1, 99)
boom_7 = ['boom' if num % 7 == 0 else num for num in numbers]
print(boom_7)

'''
# create a list that multiplies 1 through 9 by 100 
only in the number 1-9 is even

one2nine = [1, 2, 3, 4, 5, 6, 7, 8, 9]

first_list = [ele * 100 for ele in one2nine if ele % 2 == 0]
print(first_list)'''

ex4 = list(map(lambda x: x * 100, filter(lambda i: i % 2 == 0, range(1, 10))))
print(ex4)

# LAMBDA WITH IF ELSE
ex4 = list(map(lambda x: x * 100 if x % 2 == 0 else x, range(1, 10)))
print(ex4)

seven_boom = list(map(lambda x: 'boom' if x % 7 == 0 else x, range(1, 100)))
print(seven_boom)

# function sum receives 2 nums returns sum
sum2 = lambda x, y: x + y
print(sum2(2, 8))

# all combination (1,1)(6,6)
comb = []

for i in range(1, 7):
    for j in range(1, 7):
        comb.append((i, j))
print('1:', comb)

comb2 = [(i, j) for i in range(1, 7) for j in range(1, 7)]
print('2:', comb2)

#

languages = ['html', 'javascript', 'python']

print(list(filter(lambda x: x == 'python', languages)))

# JAOUL

jouls = [5000, 8000, 10000, 6000, 12000]

new = [(ej, kk) for ej in jouls for kk in list(map(lambda x: x / 4184, jouls))]
print(new)

new2 = [(j, cal) for (j, cal) in zip(jouls, list(map(lambda x: x / 4184, jouls)))]
print(new2)

