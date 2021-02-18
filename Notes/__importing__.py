import __name__

#running code from __name__.py file
# anything after will be running directly from main

__name__.main()
#this will be running from main because i called it in main]
#but it was definrs in imported file

#more about importing

#It’s possible to import only certain variables or functions from a given module. Pulling in just a single function from a module is called a function import, and it’s done with the from keyword:
#from module import function
from math import sqrt
#this way i dont have to imprt math and then call math each time i want to use it - 
# mat.sqrt()

#UNIVERSAL improting
'''
What if we still want all of the variables and functions in a module but don’t want to have to constantly type math.?

Universal import can handle this for you. The syntax for this is:
'''

# from module import *
# problem - if i def fun named like one of the 
#math fun but i import all .math so thers no need for the specification i have 2 funcs named the same
#also if i import from mulitple modukes i wont know which func is related to which module
everything = dir(__name__)
print('all imports from __name__:\n', everything, '\n')

import math
maths = dir(math)
print('all imports from math:\n' ,maths)