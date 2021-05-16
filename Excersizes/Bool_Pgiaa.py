# how to do this with pythonic way??????????
import random
import string

letters = string.ascii_lowercase


def randomize_string(): # i dont know how to one line for loop create a string
    new_list = [''.join(random.choice(letters)) for i in range(6)]
    new_string = ''
    new_string = new_string.join(new_list)
    return new_string


def receive_guess():
    guess = input('please enter guess string:\n>>>')
    if isinstance(guess, str):
        return guess
    else:
        print('what are u doing')
        return TypeError


def buul_pgiaa(real, guess):
    pgiaa = 0
    buul = 0
    matching = 0
    length_guess = len(guess)
    length_real = len(real)
    min_length = min(length_guess, length_real)

    for i in range(0, min_length -1):
        if real[i] == guess[i]:
            buul += 1

    for letter1 in real:
        for letter2 in guess:
            if letter1 == letter2:
                matching += 1

    pgiaa = matching - buul

    print(f'bool: {buul}\npgiaa: {pgiaa}')


def play_game():
    the_guess = receive_guess()
    the_string = randomize_string()

    buul_pgiaa(the_string, the_guess)
    print('the strings were: ',the_string, the_guess)

play_game()