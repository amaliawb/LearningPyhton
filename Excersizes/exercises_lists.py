#exercises_lists.py
#Exercise Question 1: Given a Python list 
#you should be able to display Python list 
#in the following order
aLsit = [100, 200, 300, 400, 500]
aLsit = aLsit[::-1]
print(aLsit)

#Exercise Question 6: 
#Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#filter is an itaretor for 
#filter(function tetst if elements of list return 
#		trueorfalse, if none idfunction returns false if any elemnts are false
#		iterable such as list)
print('remove empty from:', list1)
list_new = list(filter(None, list1))
print(list_new)

#Exercise Question 7: 
#Add item 7000 after 6000 in the following 
#Python List
list2 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list2[2][2].append(7000)
print(list2)

# Exercise Question 8: 
#Given a nested list extend it with adding sub
#list ["h", "i", "j"] in a such a way that it 
#will look like the following
#['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list3 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
extendation = ["h", "i", "j"]
list3[2][1][2].extend(extendation)
print(list3)


#Exercise Question 9: Given a Python list, 
#find value 20 in the list, and if it is present,
#replace it with 200. 
#Only update the first occurrence of a value
list4 = [5, 10, 15, 20, 25, 50, 20]
index = list4.index(20)
list4[index] = 200
print(list4)






