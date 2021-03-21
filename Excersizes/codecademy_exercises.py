# if number is even
from typing import List


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


# if number is int (if it gets str as a value it breaks because int(str) doesnt work)

def is_int(x):
    if x == int(x):
        print('trueee')
        return True
    else:
        print('falseee')
        return False


# func that recieves num and returns sum of all that nums parts:

# map() Parameter
# map(function, iterable, ...)
# function - map() passes each item of the iterable to this function.
# iterable - iterable which is to be mapped
# You can pass more than one iterable to the map() function.

# MAP = TAKES EVERY ITEM OF ITERABLE AND PASSES IT THROUGH A FUNCTION.
#       RETURNS MAP OBJECT THAT CAN BE TURNED INTO A LIST, SET, TUPLE

num = 1234


def digit_sum(n):
    """
    :param n: multiple digit number
    :return: sum of all numbers in n
    """
    # num_strlist = list(str(n)) --- will return list of all numbers as strings --- i want ints

    mapped = map(int, str(n))
    # takes the string as an iterable and returns a mapped object of all string components

    int_list = list(mapped)

    sum = 0
    for integer in int_list:
        sum += integer
    print(f'this is the sum of {n} returned:')
    return sum


print(digit_sum(num))


def factorial(n):
    """
    :param n: number
    :return: factorial of that number
    """

    num_list = [n]
    while n > 1:
        n -= 1
        num_list.append(n)
    print(num_list)
    factor = 1
    for num in num_list:
        factor *= num
    print(f'this is factorial of what u chose: {factor}')
    return factor


factorial(4)
# Can maybe multiply factorial if the loop instead of making list
'''
Define a function called is_prime that takes a number x as input.

For each number n from 2 to x - 1, test if x is evenly divisible by n.

If it is, return False.

If none of them are, then return True.'''


def is_prime(x):
    """
    if false - isnt prime
    if true - is prime
    :param x: number to check if prime
    :return: T/F if number is prime
    """
    prime_state = True

    if x > 1:
        for factor in range(2, x - 1):
            if x % factor == 0:
                prime_state = False  # not prime
                break
    else:
        prime_state = False

    if prime_state:
        print('yes prime')
    else:
        print('prime no')
    return prime_state


is_prime(11)


def is_prine_2(x):
    if x < 2:
        return False
    else:
        for factor in range(2, x - 1):
            if x % factor == 0:
                return False
                # if the division doesnt =0 it goes back to the next factor and tries. until no more factors and then its prime.
        return True


print(is_prine_2(6))

'''
Define a function called reverse that takes a string text and returns that string in reverse. For example: reverse("abcd") should return "dcba".

You may not use reversed or [::-1] to help you with this.

You may get a string containing special characters (for example, !, @, or #).
'''


def reverse(text):
    new = ''
    last_index = len(text) - 1
    while last_index >= 0:
        new += text[last_index]
        last_index -= 1

    return new


print(reverse('hello'))

'''Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.

For example: anti_vowel("Hey You!") should return "Hy Y!". Don’t count Y as a vowel. Make sure to remove lowercase and uppercase vowels.'''


def anti_vowel(text):
    vowels = ['a', 'A', 'i', 'I', 'o', 'O', 'e', 'E', 'u', 'U']
    new_text = str(text)
    for letter in text:
        if letter in vowels:
            new_text = new_text.replace(letter, "")
    print(new_text)
    return new_text
    # how to do it whithout having uppercase in vowels list???????


anti_vowel('Hey YOU,!')

'''Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word.
scrabble - each word is worth as many points as the sum of its letters worth.

Assume your input is only one word containing no spaces or punctuation.
As mentioned, no need to worry about score multipliers!
Your function should work even if the letters you get are uppercase, lowercase, or a mix.
Assume that you’re only given non-empty strings.'''

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def scrabble_score(string):
    sum = 0
    for letter in string.lower():
        sum += score[letter]
    print(sum)
    return sum


scrabble_score('Helix')

'''
def anti_vowel(text):
    vowels = ['a','A','i','I','o','O','e','E', 'u', 'U']
    new_text = list(text)
    current = 0
    for letter in new_text:
        for vowel in vowels:
            if letter == vowel:
                new_text.remove(new_text[current])
        current += 1

    text = ''.join(new_text)
    print(text)
    return text

anti_vowel('h hi hi hi hi hiiii hii oo')'''


def censor(text, word):
    if word in text:
        new_text = text.replace(word, len(word) * '*')
        print(new_text)
        return new_text


censor('you are bitch', 'bitch')

'''Define a function called count that has two arguments called sequence and item.

Return the number of times the item occurs in the list.

For example: count([1, 2, 1, 1], 1) should return 3 (because 1 appears 3 times in the list).

There is a list method in Python that you can use for this, but you should do it the long way for practice.
Your function should return an integer.
The item you input may be an integer, string, float, or even another list!
Be careful not to use list as a variable name in your code—it’s a reserved word in Python!'''


def count(sequence, item):
    dcount = 0

    for i in sequence:
        if i == item:
            dcount += 1
    print(dcount)
    return dcount


count(['hello', 'yes'], 'hello')

'''Define a function called purify that takes in a list of numbers, removes all odd numbers in the list,
and returns the result. For example, purify([1,2,3]) should return [2].
Do not directly modify the list you are given as input; instead, return a new list with only the even numbers.'''


def purify(num_list):
    new_list = []
    for number in num_list:
        if number % 2 == 0:
            new_list.append(number)
    print(new_list)
    return new_list


purify([2, 3, 4, 5, 6])

'''Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list.
 For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).

Don’t worry about the list being empty.
Your function should return an integer.'''


def product(int_list):
    pro = 1
    for ele in int_list:
        pro *= ele
    print(pro)
    return pro


product([2, 3, 4])

'''Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.

For example: remove_duplicates([1, 1, 2, 2]) should return [1, 2].

Don’t remove every occurrence, since you need to keep a single occurrence of a number.
The order in which you present your output does not matter. So returning [1, 2, 3] is the same as returning [3, 1, 2].
Do not modify the list you take as input! Instead, return a new list.'''


def remove_duplicates(input_lst):
    if input_lst == []:
        return []

    input_lst = sorted(input_lst)

    output_lst = [input_lst[0]] # starts at first element of input list
    print(output_lst)

    # only append element from sorted input to output if it is bigger than the last element of output

    for ele in input_lst:
        if ele > output_lst[-1]:
            output_lst.append(ele)

    print(output_lst)
    return output_lst


remove_duplicates([1, 2, 2, 1, 3, 4, 3, 4])


def median(lst):
  lst = sorted(lst)
  lst_len = len(lst)
  if lst_len % 2 == 0:
    middle1 = lst[lst_len / 2]
    middle2 = lst[(lst_len /2) - 1]
    return (middle1 + middle2) / 2.0
  else:
    middle_index = ((lst_len + 1) / 2) - 1
    return lst[middle_index]