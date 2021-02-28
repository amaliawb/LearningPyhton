# loops man
'''
for variable in list_name:
  # Do stuff!
  A variable name follows the for keyword; it will be assigned the value of each list item in turn.
'''

'''
iteratition:
for item in list:
  print item
  
for i in range(len(list)):
  print list[i]
'''

# FOR
# running on idexes:
n = [3, 5, 7]

for i in range(0, len(n)):
    print('i am runnig on the indexes of a list: ', n[i])

    n = [3, 5, 7]


def total(numbers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
    return result

# DOUBLE FOR
# make list out of 2 list of 2 lists
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flatten(lists):
    results = []
    for lst in lists:
        for numbers in lst:
            results.append(numbers)
    return results


print
flatten(n)