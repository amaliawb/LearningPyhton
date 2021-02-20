# list_mainpulation.py
list = [1, 2, 3, 4, 5, 6, 7, 8]

list.append(9)  # adds 9 to the end
print(list)

list.insert(2, 2.5)  # (index, data inserted) inserted 2.5 in index 2
print(list)

list.remove(3)  # remove element from lis (not index)
print(list)
list.remove(list[2])  # remove element at index 2
print(list)

print('from 0 to 4th element:', list[:5])

print('last element:', list[-1])

# to know what is the index of an element
print(list)
print('what is the index of the element 4?:', list.index(4))
# two lists in relation have one value in other find same value in the second one


# how many of x is in list
list.append(5)
print('5 is in list %d times' % list.count(5))

# SORT -
list.append(3)
list.remove(5)
print('not sorted', list)
print(sorted(list), 'this is the sorted list but it wanst re-saved')
# print('un sort the sorted',sorted(list, reverse = True))
list.sort()  # cant print it beacuse is actively saving new list
print('nums sorted', list)

list2 = ['carina', 'amanda', 'nahman', 'lola']
list2.sort()
print('names alphabetically sorted:', list2)

# lists within lists - TWO DIMENSINAL

list3 = [
    [5, 6], [6, 7], [4, 6]
]
print(list3)
print(list3[1][1])  # 1st element -> 1st elemnt

users = ['john', 'amy', 'brad']
ages = [12, 24, 36]

print(users.pop())  # removes last element on list
print(users)
users.insert(1, 'jenna')
print(users)

# combine users and ages
users_and_ages = users + ages
print(users_and_ages)

del (users[2])  # deletes
print(users)

# copys
num = [1, 2, 3, 4]
num2 = []
print(f'num1 is {num}, num2 is {num2}')
print('copying...')
num2 = num[:]
print(f' after copy num1 is {num}, num2 is {num2}')
