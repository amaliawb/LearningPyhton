def convert(string):
    roman_letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    str_length = len(string)
    return_sum = 0

    for i in range(str_length):
        int_value = roman_letters[string[i]]
        if i + 1 < str_length and roman_letters[string[i + 1]] > int_value:
            return_sum -= int_value
        else:
            return_sum += int_value
    print(return_sum)

convert('XLIX')