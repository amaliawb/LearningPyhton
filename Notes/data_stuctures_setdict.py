#data_stuctures_setdict

#set = values that have no order or index
#	doesnt allow double values
set1 = set(['orange', 'green', 'green', 'blue'])
print(set1)


#dictionary = values of no order
#	there is an index
#	can be changed 
#	cant have double values

dict1 = {'Name':'Amalia', 'City':'Tel Aviv'}
print(dict1)

example = set()
print(dir(example)) #prints all methods i can use on example set
print(help(example.add)) #explains method
print(example)

example.add(42)
example.add(False)
example.add('hi')
example.add(42) #will still have it one time

print(example)
print(len(example))

example.remove(42) #will throw an error if element isnt in the set
print(len(example))

help(example.discard) #will discard element only if its in the set - wont throw error if it isnt

example.clear() #deleted all elements
print(example)

# two sets:
# set1 + set 2 uniun is 1U2
# set 1 and set 2 intersection is 1Uhafuch2

odds = set([1,3,5,7,9])
evens = set([2,4,6,8,10])
primes = set([2,3,5,7])
composites = set([4,6,8,9,10]) #can be factored

print(odds.union(evens)) #set of all numbers
print(odds.intersection(primes))
print(primes.intersection(evens))

# is element in set
print(2 in primes) #true
print(6 in odds)
print(3 not in evens)

#DICTIONARIES

my_info = {'name':'Amalia', 'age':'20', 'courses':['Python', 'Java']}
print(my_info)
print(my_info['name'])
print(my_info['courses'])

#if you try to access key that doesnt exist
#it will throw KeyError
#to avoid this use .get()
help(my_info.get)
print(my_info.get('name'))
print(my_info.get('phone')) 
#returns none when key isnt specified
print(my_info.get('phone', 'not found...')) 











