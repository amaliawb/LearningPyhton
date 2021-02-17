methods

# LOWER/UPPER CASE method
print(message.lower()) # running lower methos on the string
print(message.upper()) # same

# COUNT method - counts number of times the word passed as arg repeats in str 
print(message.count('multiple'))
print(message.count('m'))

#FIND method- finds the index of the first letter of str i want to find
print(message.find('print'))
print(message.find('amalia'))
# will print -1 means no

#REPLACE method -
message = ('Hi , I am Amalia')
print(message)
new_message = message.replace('I am' , 'my name is') #need to set new var to get return value, cant just replace and print message. does not change messgae, sets new return value to new var
print(new_message)
# to change message u need to set var again
message = message.replace('I am' , 'my name is')
print(message)

# concatinate strings together
greeting = 'hello'
name = 'amalia'
message = greeting + ', ' + name + '. welcome' # need to add space 
print(message)

#FORMAT method - formatted string to make vars readable     
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)
#in py 2 fomatting is done with % insteaed of {} an no method
#%s for strings %d for decimals and %0X nums from 0 to 2 places after
#print('Hello my name %s i am %s old') % (amalia, 20)

#fstrings - from py 3.6 and above - make str formatting easy
message = f'{greeting}, {name}. WELCOME'
print(message)