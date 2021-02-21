# rot 13

def make_dictionary(rot_num):
    new_dict = {}
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 0+13 = n
    for letter in alphabet_lower:
        if letter <= alphabet_lower[12]:
            new_dict[letter] = alphabet_lower[alphabet_lower.index(letter) + rot_num]
        elif letter >= alphabet_lower[12]:
            new_dict[letter] = alphabet_lower[alphabet_lower.index(letter) - rot_num]
    for letter in alphabet_upper:
        if letter <= alphabet_upper[12]:
            new_dict[letter] = alphabet_upper[alphabet_upper.index(letter) + rot_num]
        elif letter >= alphabet_upper[12]:
            new_dict[letter] = alphabet_upper[alphabet_upper.index(letter) - rot_num]
    return new_dict


# made rot dict maker!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def encode(str):
    dict13 = make_dictionary(13)
    if len(str) > 8 and str.isalpha():
        print('no')
    else:

print(encode('sdk'))
