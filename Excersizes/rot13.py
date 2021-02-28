# rot 13
MAX_LETTER_JUMP = 12

# alphabets
alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = alphabet_lower.upper()

# keys for dict
keys = list(alphabet_lower + alphabet_upper)


# translated string
def rotated_alphabet(alphabet, rot_num):
    rotated = ''
    for letter in alphabet:
        if letter <= alphabet[MAX_LETTER_JUMP]:
            rotated += alphabet[alphabet.index(letter) + rot_num]
        elif letter >= alphabet[MAX_LETTER_JUMP]:
            rotated += alphabet[alphabet.index(letter) - rot_num]
    return rotated


# calling the function values for dict keys - accordingly
values = rotated_alphabet(alphabet_lower, 13)
values += rotated_alphabet(alphabet_upper, 13)


# make dictionary
def make_dict(keys, values):
    return dict(zip(keys, values))


rot13_dict = make_dict(keys, values)


def input_translator():
    users_string = input("Please enter message to encode:\n>>>")
    new_str = ''
    for letter in users_string:
        new_str += rot13_dict[letter]
    print('this is your encoded str: {}'.format(new_str))

input_translator()


