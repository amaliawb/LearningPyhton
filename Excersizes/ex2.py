# excercise 2 - lesson 3 - random

import random #imports random module

def get_guess(num):

    guess = int(input('Enter a number:\n>>> '))
    if guess == num:
        print('you won')
    else:
        print('u lost')


def randomize_to_guess():
    num = random.randint(1, 100)
    get_guess(num)


randomize_to_guess()








''' wrong that i did: needed to make func for getting guess and func for random num, call getting guess inside random number



def guessing_game(num):
    x = random.randint(0,10)
    
    num = int(num)
    if 0 <= num <= 10:
        if num == x:
            print('YOU WON!')
        else:
            print('Oh No! You Lost')

    else:
        print('num between 0 - 10, try again')
        


guess = input('I thought of a number. Try and guess it:\n>>>')
guessing_game(guess)



def info_on_guess(num):
    rand = random.randint(0,10)
    num = int(num)
    if num > rand:
        print('ur num is bigger than mine')
    elif num < rand:
        print('ur num is smaller than mine')
    else:
        print('ur num is my num')
        


guess_two = input('again:\n>>>')
info_on_guess(guess_two)

'''

