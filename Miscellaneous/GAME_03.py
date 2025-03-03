import time
import random
import os
FilePath = os.getcwd()
textfile = os.path.join(FilePath,"ARCHIVE","[MISC] Memory.txt")

if os.path.exists(textfile):
    print("{} exist".format(textfile))
else:
    print("{} Does not exist".format(textfile))


# Testing if dictionary works within a text file
Memory = {"Apple": 1.50, "Orange": 2.55, "Banana": 4.25}

with open(textfile, "w") as file:
    file.write(str(Memory))

with open(textfile, "r") as file:
    content = file.read()


content = {}

print(content)

for food, price in Memory.items():
    content[f"{food}"] = price

print(content)

if content == Memory:
    print("")