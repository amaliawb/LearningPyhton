# lambda expressions
# only one line function
# makes itirating easier
# instead of loops

# lambda arguments: expression


result = map(lambda x: x ** 2, [1, 2, 4, 99])
print(list(result))

#        func that recieves a 

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2, my_list))

print(new_list)

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print(new_list)

# PYTHONIC WAY EXPLANATION

add = lambda num1, num2: num1 + num2
# function has no name - we assign it to var add and now add is looking at this function
# mapping to this function
print('using lambda on var add(3,4) = ', add(3, 4))

# real example with
# MAP
# map(function to apply on all elements of, iterable)

rslt = list(map(lambda x: x ** 2, range(5)))
print('using lambda function as func in map():', rslt)

# iterating dicts
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

map(lambda x: x['name'], dict_a)  # Output: ['python', 'java']

map(lambda x: x['points'] * 10, dict_a)  # Output: [100, 80]

map(lambda x: x['name'] == "python", dict_a)  # Output: [True, False]

# multiple iterables
list_a = [1, 2, 3]
list_b = [10, 20, 30]

map(lambda x, y: x + y, list_a, list_b)  # Output: [11, 22, 33]

# FILTER
# filter(func,iterable) func returns true or false on all elements of iterable
# filter out all False returns

alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = filter(lambda x: x % 2 == 0, alist)
print('filtered list with lambda:', list(filtered))

# filter dicts
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

f2 = filter(lambda x: x['name'] == 'python', dict_a)  # Output: [{'name': 'python', 'points': 10}]

print(list(f2))