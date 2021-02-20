# data_stuctures_setdict

# important -
'''
lists -
.index("item in list i want to get its index")
.insert(index of insert, "item to insert") - pushes all after index by 1
.sort()
.remove("item to remove")

dictionaries -
del dictName[keyName]
'''

inventory = {'gold': 500, 'pouch': ['flint', 'twine', 'gemstone'],
             'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf'],
             'burlap bag': ['apple', 'small ruby', 'three-toed sloth']}

# Adding a key 'burlap bag' and assigning a list to it

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50
print(inventory)
# set = values that have no order or index
#	doesnt allow double values
set1 = set(['orange', 'green', 'green', 'blue'])
print(set1)

# dictionary = values of no order
#	there is an index
#	can be changed 
#	cant have double values

dict1 = {'Name': 'Amalia', 'City': 'Tel Aviv'}
print(dict1)

example = set()
print(dir(example))  # prints all methods i can use on example set
print(help(example.add))  # explains method
print(example)

example.add(42)
example.add(False)
example.add('hi')
example.add(42)  # will still have it one time

print(example)
print(len(example))

example.remove(42)  # will throw an error if element isnt in the set
print(len(example))

help(example.discard)  # will discard element only if its in the set - wont throw error if it isnt

example.clear()  # deleted all elements
print(example)

# two sets:
# set1 + set 2 uniun is 1U2
# set 1 and set 2 intersection is 1Uhafuch2

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])  # can be factored

print(odds.union(evens))  # set of all numbers
print(odds.intersection(primes))
print(primes.intersection(evens))

# is element in set
print(2 in primes)  # true
print(6 in odds)
print(3 not in evens)

# DICTIONARIES

my_info = {'name': 'Amalia', 'age': '20', 'courses': ['Python', 'Java']}
print(my_info)
print(my_info['name'])
print(my_info['courses'])

# if you try to access key that doesnt exist
# it will throw KeyError
# to avoid this use .get()
# help(my_info.get)

print(my_info.get('name'))
print(my_info.get('phone'))
# returns none when key isnt specified
print(my_info.get('phone', 'not found...'))

my_info['phone'] = '0544688057'
print(my_info)
# UPDATING VALUES IN DICT
# 1. assign indices
# .update function.
my_info['name'] = 'Bloch'
print(my_info)
my_info.update({'name': 'amalia', 'age': '21', 'phone': '9724688057'})
print(my_info)

# print(dir(my_info))

# delete

del my_info['phone']
print('\n\n\n', my_info)

age = my_info.pop('age')  # popped off and saved into var
print(my_info)
print(age)

my_info.update({'name': 'Amalia', 'age': '21', 'phone': '9724688057'})

# loop through dict
print('\n\n' + str(len(my_info)))
print(my_info.keys())
print(my_info.values())
print(my_info.items())

for key in my_info:  # will hust print keys
    print(key)
print('\n')

for key, value in my_info.items():  # will print whole dict
    print(key, value)

# dict for loop
# A simple dictionary
d = {"foo": "bar"}

for key in d:
    print
    d[key]  # prints "bar"

# 2 example of list with for loop
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in a:
  if a[i] % 2 == 0:
    print(a[i])