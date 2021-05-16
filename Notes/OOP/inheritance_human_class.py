# INHERITANCE
class human():
    """this is a human class"""

    def __init__(self, gender="human", age=0):
        """constuctor: these are humans attributes initiated"""
        self.gender = gender
        self.age = age

    def speak(self):
        print(f"from human class: Hi I am a {self.gender}, and I am {self.age} years old")


class man(human):
    """man subclass"""

    def __init__(self, hairColour, age):  # add more attr to be defined at class object initiation
        super().__init__(gender="Male", age=age) # added age attr to init, in order to manipulate age in parent class u need to add it to super constructor
        """super constructor allows to inherit humans attr and overwrite the gender"""
        self.hair = hairColour
        # add new attr - define in constructor like hair
        # manipulate parnet attr - define in constructor and call or change in super constructor


    # overwrite methods
    def speak(self):
        print(f"after mothod overwrite from man class: I am a {self.gender}, and I am {self.age} years old")



class woman(human):
    """woman subclass"""

    def __init__(self, hairColour):
        super().__init__(gender="Female")
        self.hair = hairColour


bob = man("brown", 30) # hair is defined in assignment
bobette = woman("blonde")
bob.speak()
bobette.speak()
print(f"bobs hair is {bob.hair}")
print(f"bobettes hair is {bobette.hair}")
