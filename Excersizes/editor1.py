# home excercise 1 - lesson 3 SHE CODES!

print('Hello! please follow the directions below:\n')

name = input('Enter your name:\n>>> ')
surname = input('Enter your surname:\n>>> ')
birth_year = input('Enter your birth year:\n>>> ')

def make_initials(str1, str2):
    if len(str1) > 0 and len(str2) > 0 and str1.isalpha() and str2.isalpha():
        str1 = str1.upper()
        str2 = str2.upper()
        return str1[0] + str2[0]
    else:
        print('try again...')

def age_calc(year):
    if len(year) == 4:
        year = int(year)
        return 2021 - year
    else:
        print('try again...')
    
    

initials = make_initials(name, surname)
age = str(age_calc(birth_year))

print(f'Your initials are {initials} and you are {age} years old')
