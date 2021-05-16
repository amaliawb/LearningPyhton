# TF is a class
'''assignament statements produces an object
a = 2 produces an object - what kind of object? integer object is created
integer class is somthing that will inform the object what it is going to look like
when object is cretaed it gets : name a
1. ID number
2. TYPE: <class 'int'>
3. VALUE: 2
the integer class type informs the object what it is like a blue print
but after creating it is independent
object exist in exe space in its own right
the name is bound to the obj that contains the value

'''

# int class:
# attributes are ID, type and value
# i define attributes in def __init__ constructor when creating a class

print('attributes of var a:')
a = 2
print(id(a))
print(type(a))  # locates the label a then locate type and print it
print(a)

# assignment -> integer class produces an object thats labeled a
# class is like a blue print that allows types of variables to be their type - int string whatever

# two vars same value - create 1 object, use two labels on 1 object
a = 2
b = 2
print('\na and b are the same object - same id:', id(a), id(b))

# same for floats, strings

c = 3.3323232323232323232323232323232323247245726456745628745628475628734582354827345682756287346827346582735462873456283746234982345023572984358484884848934898943893489893483895757854784893489438948329093209032903223903290239
print(type(c))

# assignament - reassignment doesnt replace the value

d = 3
# b is a NAME with a BINDING to the INT OBJECT 3
# x titled object is cretaed using the int class
# the object is an immutable object cannot be altered once created - cannot change is value
# if i want to reassign another object will be created - the label will be moved to the other obj.
# old x is unnamed and python will mark it 4 garbage collection - eventually removed

y = 2
y = y + 1


# calculation are done in the ARITHMETIC AND LOGIC UNIT
# y+1 is calculated in the ALU:
# moves the value of y to the ALU
# takes 1 and adds it and gives result of 3 , creates new object 3 that gets label y and removes label y from old 2


# OOP
# creating classes - templates for kinds of object that are similar in your program
# describing a class:
# 1. class name
# 2. attributes - whats it like
# 3. methods - what it does functions

# INHERITANCE
# classes can inherit attributes and methods(behaviors) of another class
# subclasses = classes that inherited attr from othe classes
# to inherit attr you need 1. define it, 2. define super constructor
"""
class subclass(superclass):
    def __init__(self):
        super().__init__(<any changes to attr inherited>)
"""

# CALCULATOR

class calc:
    def add(x, y):
        added = x + y
        return added

    def sub(x, y):
        sub = x - y
        return sub

    def multi(x, y):
        mult = x * y
        return mult


print('\n\nCLASSES: calculator')
print('multiplication defined in class calc:', calc.multi(3, 4))
print('subtraction:', calc.sub(10, 9))


class human():
    """this is a human class"""

    # constructor like little function that will construct
    # the classes attributes - initiates all attributes as default values
    def __init__(self, human_gender='unknown', age=0, hangry_level='peaceful', hunger_level=0):
        self.human_gender = human_gender
        self.age = age
        self.hangry_level = hangry_level
        self.hunger_level = hunger_level

    # add methods
    def setGender(self):
        self.human_gender = str(input('set humans gender:\n>>>'))

    def setAge(self):
        self.age = int(input('set age:\n >>>'))

    def setHunger(self):
        self.hunger_level = int(input('set hunger level (0-10):\n>>>'))

    def changeHangry(self):
        if 0 <= self.hunger_level < 4:
            self.hangry_level = 'currently peaceful'
        elif 4 <= self.hunger_level < 8:
            self.hangry_level = 'getting narky'
        elif 8 <= self.hunger_level <= 10:
            self.hangry_level = 'EEMALE humans so hangry now'

        return self.hangry_level


# create an object from class
print('\ncreating an object with my human class: mr. smith = new object\n')
MrSmith = human()  # CREATE OBJECT = mr smith is an object set from <class human>
MrSmith.setGender()  # ACCESS METHODS = using methods from the class to define attributes (like using methods on strings like string.join()
MrSmith.setAge()
MrSmith.setHunger()
MrSmith.changeHangry()
# ACCESS ATTRIBUTES:
print(f'HUMAN:\nName: {MrSmith.human_gender}\nAge: {MrSmith.age}\nIs Hangry?: {MrSmith.hangry_level}', )
