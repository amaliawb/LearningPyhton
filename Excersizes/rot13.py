# rot 13
# cr

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
    print(dict13)
    new_str = ''
    # if str.isalpha():
    for letter in str:
        if letter == ' ':
            new_str += ' '
        else:
            new_str += dict13[letter]
    return new_str


print(encode('V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL'))
