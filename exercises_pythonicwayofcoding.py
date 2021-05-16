# ex 1 : sikul otiot
# string 1 amalia string 2 aliama is it sikul?

'''
run on all letters of strings
sort all letters
'''

str1 = 'sorted'
str2 = 'dtesor'


def sikul_id(str1, str2):
    sorted1 = sorted(str1)
    sorted2 = sorted(str2)
    if sorted1 == sorted2:
        print('is sikul')
        return True


sikul_id(str1, str2)

# ex3
# recieves list of numbers returns list of number +1


def make_num(list1):
    if isinstance(list1, list):
        added_str = str(int(''.join(str(num) for num in list1)) + 1)
        splited = list(int(num) for num in added_str)

        return splited


print(make_num([1, 0]))
