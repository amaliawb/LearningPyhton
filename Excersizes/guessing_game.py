import random
def calc_guess(num):
    """
    :param num: receives number
        ask for input user number
    :return: if users number is num
    """
    guess = int(input('Enter a number:\n>>> '))
    count = 1
    while guess != num:
        if guess > num:
            print(f'you lost: {guess} is bigger than the winner')
        elif guess < num:
            print(f'you lost: {guess} is smaller than the winner')

        guess = int(input('Guess again:\n>>>'))
        count += 1

    if guess == num:
        print(f'you won with {count} tries')


def guessing_game():
    num = random.randint(1, 100) # randomises number
    calc_guess(num) # puts randomised number inside calc_guess to receive input and compare to random

guessing_game()
