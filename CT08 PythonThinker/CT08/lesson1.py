class style():

    BOLD = '\033[1m'
    ITALIC = '\033[3m'

    UNDERLINE = '\033[4m'
    CANCEL = '\033[9m'

    bgbwhite = '\033[7m'

    black = '\033[8m'
    bgray = '\033[30m'
    dred = '\033[31m'
    dgreen = '\033[32m'
    dyellow = '\033[33m'
    dblue = '\033[34m'
    dpurple = '\033[35m'
    dcyan = '\033[36m'
    dwhite = '\033[37m'

    bgray = '\033[90m'
    bred = '\033[91m'
    bgreen = '\033[92m'
    byellow = '\033[93m'
    bblue = '\033[94m'
    bpurple = '\033[95m'
    bcyan = '\033[96m'
    bwhite = '\033[97m'

    RESET = '\033[0m'

    # Generic Colours
    primary = dblue
    secondary = bgray
    
    warning = dyellow
    error = dred
LINE = style.bgray + "------------------------------" + style.RESET


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


# -- Learning Exercise 1: A simple class with a constructor

class ZooAnimal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    
lion = ZooAnimal("Leo","Lion")
# lion is a child of ZooAnimal

print(f"Animal: {lion.name} | Species: {lion.species}")

# -- Learning Exercise 2: Add a method
class ZooAnimal2:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    # Describing a method
    def describe(self):
        print(f"Animal: {self.name} | Species: {self.species}")
    
Elephant = ZooAnimal2("Ellie","Elephant")
# lion is a child of ZooAnimal

Elephant.describe()

# -- Learning Exercise 3: 
class ZooAnimal3:
    def __init__(self,name: str,species: str, diet: str):
        self.name = name
        self.species = species
        self.diet = diet

    def describe(self):
        print(f"Animal: {self.name} | Species: {self.species}")

    def hungry(self):
        print(f"{self.name} ate {self.diet}")

Elephant = ZooAnimal3("Ellie","Elephant","Grass")
# lion is a child of ZooAnimal

Elephant.describe()
Elephant.hungry()