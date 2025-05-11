# -- Classes and Object Oriented Programming [OOP]
    # OOP is a way of organizing code that is based on real-world objects.
    # A Class will have Attribute and Behaviour
    # Class: A blueprint that defines what an object should have and what it can do.

# Instead of:
Placeholder = {
    "NAME":{
        "behaviour1":"behaviour1",
        "behaviour2":"behaviour2",
        "behaviour3":"behaviour3"
    }
}

# We can do:
class Placeholder:
    def __init__(self,behaviour1,behaviour2,behaviour3):
        self.behaviour1 = behaviour1
        self.behaviour2 = behaviour2
        self.behaviour3 = behaviour3

    def printattributes(self):
        print(f"{self.behaviour1},{self.behaviour2},{self.behaviour3}")

name1 = Placeholder("T1","T2","T3")
name1.printattributes()
# 'self' represents the instance of the class on which the method is called. 