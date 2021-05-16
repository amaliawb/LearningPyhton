# CAT CLASS
# class implementation:
class Cat:
    # constructor
    # declare attributes provided in cat
    # self is pointing to  the object later created with the class cat to reference to it
    def __init__(self, name: object = 'unknown', age: object = 'unknown', weight: object = 'unknown') -> object:
        self.name = name
        self.age = age
        self.weight = weight
        self.stomach = 0

    def get_name(self):
        return self.name

    def speak(self):
        """checks if cat is hungry based on stomach amount
        returns if hungry or not"""
        if self.stomach > 0:
            return 'Prrrrr...'
        else:
            return 'Meow!!!!!!!!!'

    def feed(self, amount):
        """ feed SELF amount food
        which cat should i feed this amount in pounds (int)"""
        self.stomach = self.stomach + amount

    def next_day(self):
        """keep a cat alive
        cat gets skinnier each day that passes
        every day 1/4 pound skinnier
        resets stomach"""
        self.weight += self.stomach - 0.25
        self.stomach = 0

    def get_weight(self):
        return self.weight


def main():
    cat1 = Cat('Shelly', 13, 100)
    cat2 = Cat('Mushka', 25, 15.6)

    print(cat1.get_name(), 'says', cat1.speak())
    print(cat2.get_name(), 'says', cat2.speak())

    cat1.feed(5)
    cat2.feed(0.50)

    print(cat1.get_name(), 'says', cat1.speak(), 'i weigh', cat1.get_weight())
    print(cat2.get_name(), 'says', cat2.speak(), 'i weigh', cat2.get_weight())

    cat1.next_day()
    cat2.next_day()

    print(cat1.get_name(), 'says', cat1.speak(), 'i weigh', cat1.get_weight())
    print(cat2.get_name(), 'says', cat2.speak(), 'i weigh', cat2.get_weight())


# if this file is the main file and not an imported file then
# execute what is in "main" function
if __name__ == "__main__":
    main()
