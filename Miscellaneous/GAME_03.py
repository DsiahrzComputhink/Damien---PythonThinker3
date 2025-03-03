import time
import random
import os
FilePath = os.getcwd()
textfile = os.path.join(FilePath,"ARCHIVE","L07-File_Input\Output [example].txt")

if os.path.exists(textfile):
    print("{} exist".format(textfile))
else:
    print("{} Does not exist".format(textfile))

# Note to self:
    # file = open(textfile, "w") # the "w" means writes data to the file
    # file = open(textfile, "r") # the "r" means read the file
    # file = open(textfile, "a") # the "a" means appends data to a file

# Excercise 1: Write to a file
file = open(textfile, "w")
file.write("Hello world\n")
file.close()

# Excercise 2: Read from a file
file = open(textfile, "r")
content = file.read()
# print(f"File content:\n {content}")
file.close()

# Excercise 3: Using the 'with keyboard
with open(textfile, "r") as file:
    content = file.read()
    # print(f"File content with 'with': {content}")

# print(content)

# Excercise 4: Append to file
with open(textfile, "a") as file:
    file.write("\nThis will add a new line to the file")
    file.write("\nThis will add another line.")
    file.write("\nThis will add another new line.")
    
# Excercise 5: Write multiple Lines
lines = ["Line1\n","Line2\n","Line3\n"]

with open(textfile, "w") as file:
    file.writelines(lines)

with open(textfile, "a") as file:
    file.write("Number Sequence\n")
num = -1
for i in range(10):
    num += 1
    with open(textfile, "a") as file:
        file.write(f"{num}  ")
        file.write("Testing\n")

with open(textfile, "w") as file:
    file.write("1 2 3 4 5")

with open(textfile, "r") as file:
    content = file.read()

print(content)
if content == "1 2 3 4 5":
    print("Content is '1 2 3 4 5'")
else:
    print("Content is not '1 2 3 4 5'")

# Testing if dictionary works
fruitcost = {"Apple": 1.50, "Orange": 2.55, "Banana": 4.25}

with open(textfile, "w") as file:
    file.write(str(fruitcost))

with open(textfile, "r") as file:
    content = file.read()

print(content)
content = dict
if content is dict:
    print("Content is Dictionary")
else:
    print("Content is not dictionary")