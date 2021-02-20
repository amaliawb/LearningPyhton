# dictionary_exercise

# dictionary exercise 1: Below are the two lists convert it into the dictionary

# zip(*iterables) = takes in iterables and returns tuples of indexes (1+1), (2+2)
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(dict(zip(keys, values)))

# dictionary exercise 2: Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
###other way
# dict3 = {**dict1, **dict2}


# dictionary exercise 3: Access the value of key ‘history’
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class'])
print(sampleDict['class']['student']['marks']['history'])
# print(sampleDict[0][0][1][1]) - wont work


# dictionary exercise 4: Initialize dictionary with default

# The fromkeys() method
# creates a new dictionary from the given sequence of
# elements with a value provided by the user.
# dict.fromkeys(sequence used as keys, <value set to each element)
# if only sequence is defined keys are all set to value None

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
new_dict = dict.fromkeys(employees, defaults)
print('\n', new_dict)

# dictionary exercise 5: Create a new dictionary by
# extracting the following keys from a given dictionary

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}

sampleDict.pop('name')
sampleDict.pop('salary')
print(sampleDict)

# dictionary exercise 7: Check if a value 200 exists in a dictionary
sampleDict = {'a': 100, 'b': 200, 'c': 300}
print(200 in sampleDict.values())

# dictionary exercise 8: Rename key city to location in the following dictionary
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
print(sampleDict.pop('name'))  # popping is returning removed keyvalue
sampleDict['location'] = sampleDict.pop('city')  # setting new key to return value of pop
print(sampleDict)

# dictionary exercise 9: Get the key corresponding
# to the minimum value from the following dictionary
# min(iterable, [*iterables], [key], [default])
# int dicts min returns smallest key
# min iterates all elemnts of dict given

sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print('\n')
print('get the key that its value is min:', sampleDict)
print(min(sampleDict))  # this simple work???????
print(min(sampleDict, key=sampleDict.get))
# 1
# key = lambda k: sampledict[k] uses all values as the min comparison rather than the keys
print('\n')
min_key = min(sampleDict, key=lambda k: sampleDict[k])
print('1st way - lamnda min iteration:', min_key)
# 2
# min iterates dict and chooses min by .get that takes the key values and calcs min
print('\n2nd way- using .get to choose min from values and print key:', min(sampleDict, key=sampleDict.get))

# 3
# for itearation
print('\n3nd way - for iteration on all values print only minkey')
print(min(sampleDict.values()))
for key, value in sampleDict.items():
    if value == min(sampleDict.values()):
        print(key)

# dictionary exercise 10: Given a Python dictionary,
# Change Brad’s salary to 8500
sampleDict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
sampleDict['emp3']['salary'] = 8500

print(sampleDict)

# wrong = sampleDict.update({'emp3':{'salary':8500}}) #changes whole pairs takes off name

# print(sampleDict)
