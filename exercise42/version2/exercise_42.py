"""
Is-A, Has-A, Objects, and Classes
"""


## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


## Dog is-a animal
class Dog(Animal):
    def __init__(self, name):
        ##
        self.name = name


## Cat is-a animal
class Cat(Animal):
    def __init__(self, name):
        ##
        self.name = name


## Person is-a object
class Person(object):
    def __init__(self, name):
        ##
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None


## Employee is a person
class Employee(Person):
    def __init__(self, name, salary):
        ## hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ##
        self.salary = salary


## Fish is-a object
class Fish(object):
    pass


## Salmon is-a fish
class Salmon(Fish):
    pass


## Halibu is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

##
satan = Cat("Satan")

##
mary = Person("Mary")

##
mary.pet = satan

##
frank = Employee("Frank", 120000)

##
frank.pet = rover

##
flipper = Fish()

##
crouse = Salmon()

##
harry = Halibut()
