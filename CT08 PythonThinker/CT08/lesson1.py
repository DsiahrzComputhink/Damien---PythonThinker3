# -- Classes and Object Oriented Programming [OOP]
    # OOP is a way of organizing code that is based on real-world objects.
    # A Class will have Attribute and Behaviour
    # Class: A blueprint that defines what an object should have and what it can do.

# Instead of:
Placeholder = {
    "name1":{
        "behaviour1":"T1",
        "behaviour2":"T2",
        "behaviour3":"T3"
    }
}

# We can do:
class Placeholder:
    def __init__(self,behaviour1,behaviour2,behaviour3): # 'self' represents the instance of the class on which the method is called. 
        self.behaviour1 = behaviour1
        self.behaviour2 = behaviour2
        self.behaviour3 = behaviour3

    def printattributes(self):
        print(f"{self.behaviour1},{self.behaviour2},{self.behaviour3}")
# With a class, you can create as many items as you want without re-writing code

# name1 = Placeholder("T1","T2","T3")
# name1.printattributes()

# [Advantages]:
    # Organizes Your Code:
        # Groups related data (attributes) and actions (methods) in one place

    # Reduces Repetition:
        # Defines a single class and reuses it for multiple objects

    # Easy to add Features:
        # Adds new beahviours without affecting existing code

    # Real-World Modelling:
        # Classes help you represent real-life things in your program
        # Makes the code intitutive and easy to understand
        # Each Object has their own memory

# -- Key Concepts in Classes:
    # Class: A blueprint or templatefor creating objects
        # Defines shared traits and behaviours

    # Object:
        # A specific instnce of a class

    # Attributes: 
        # Data that described a object

    # Methods:
        # Actions or behaviours that an object can perform

    # Parent Class and Child Objects:
        # A class acts as a parent, and objects are its children


# Learning Exercise 1: A simple class with a constructor

class ZooAnimal:
    def __init__(self,name,species): # 'self' represents the instance of the class on which the method is called. 
        self.name = name
        self.species = species

    def DebugAttributes(self):
        print(f"{self.name},{self.species}")
    
lion = ZooAnimal("Leo","Lion")

lion.DebugAttributes()