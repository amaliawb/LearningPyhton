#lambda expressions
#only one line function
#makes itirating easier
#instead of loops

#lambda arguments: expression


result = map(lambda x: x**2,[1,2,4,99])
print(list(result))

#        func that recieves a 

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)