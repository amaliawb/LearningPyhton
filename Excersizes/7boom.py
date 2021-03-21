def check_boom(number, input):
    # checks if turn number and input correspond
    # if turn number is %7==0 input should be boom
    # if not input should be the same turn number
    # if input is correct returns true
    if number % 7 == 0:
        if input == 'boom':
            return True
        else:
            return False

    elif number == int(input):
        return True

    else:
        return False


def comp_boom(number):
    if number % 7 == 0:
        print('boom')
    else:
        print(number)

for i in range(1, 22):

    turn = i

    if turn % 2 != 0.0:
        current_input = input("\nInsert next number:\n>>>")

        if check_boom(i, current_input):
            print(f'{current_input} is correct\n')
            continue
        else:
            print('incorrect')
            break

    else:
        print('my turn!')
        comp_boom(i)










'''
        if number % 7 == 0:
            if current_input == 'boom':
                continue
            else:
                print('wrong')
                break
        elif number == int(current_input):
            continue
        else:
            print('what??')
            break
    turnes += 1
'''