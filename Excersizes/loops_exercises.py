# LLOPS IS FUN

# 1.

def print_asterix(num):
    asterix = '*'
    print(num * asterix)
    return num * asterix


def print_triangle():
    for i in range(1, 10):
        print_asterix(i)


print_triangle()

print('\n\n\n')


def print_trapez():
    for i in range(5, 15):
        print_asterix(i)


print_trapez()


def print_meuyan():
    for i in range(6):
        if i <= 3:
           print_asterix(i)
        else:
            print_asterix()

print_meuyan()