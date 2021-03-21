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
  
  
  for somthing
  printing 'somthing',
  puts '  ' between words and not down a line
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

# more for
hobbies = []

# Add your code below!
for i in range(4):
  hobby = input('Enter hobbie: ')
  hobbies.append(hobby)
print(hobbies)

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


# While - counter loop

# while condition:
# do this
# condition += 1

# while True:
# do this
# while else: while true do this but else = while false do this
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!

while guesses_left > 0:
  guess = raw_input('enter guess: ')

  if guess == random_number:
    print 'You Win!'
    break
  guesses_left -= 1
else:
  print 'You lose.'


# BREAK

# CONTINUE
# bring you back immidiatly to the begnning of the loop without executing the rest of what is written in the loop after continue


# PASS
# do nothing, move forward in the loop ( if the pass is in if statemnet it ignores the if statement)

def string_match(a, b):
    short_str_len = min(len(a), len(b))
    count = 0
    for i in range(short_str_len - 1):
        sub_a = a[i: i + 2]
        sub_b = b[i: i + 2]
        if sub_a == sub_b:
            count += 1
    return count


print(string_match('ama', 'amaxa'))

strs = ['gagag', 'cruel', 'no', 'ahahaha']
strs.append('lala')
print(strs)

def str_list_returner(list_of_str):
    new_list = []
    for dstring in list_of_str:

        if dstring[0] == dstring[-1]:
            new_list.append(dstring)
    return new_list

print(str_list_returner(strs))

# FOR ELSE
'''
just like with while, for loops may have an else associated with them.
In this case, the else statement is executed after the for, but only if the for ends normally—that is, not with a break.
'''