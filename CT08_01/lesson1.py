# File Input / Output

    # File Modes:
        # r: Read Modes - Read the data of a file
        # w: Write Modes - Writes data to a file
        # a: Append Modes - Adds data to a file

    # File Operation: 
        # open() - Establishes a connection to a file
        # read/write/append - Processes File connection
        # close: - Frees resources after file operations

    # Advantages:
        # Persistent Storage - Retains data after the program ends
        # Flexibility - Handle various file formats (text, binary, CSV, etc)
        # Scalability - Manage large datasets efficently

    # Disadvantages:
        # Data Security - Avoid unauthorized access
        # Handling Errors - Deal with missing files or unexpected Disadvantages
        # Performance - Not optimized for large file operations

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
print(f"File content:\n {content}")
file.close()

# Excercise 3: Using the 'with keyboard
with open(textfile, "r") as file:
    content = file.read()
    print(f"File content with 'with': {content}")

print(content)

# Excercise 4: Append to file
with open(textfile, "a") as file:
    file.write("\nThis will add a new line to the file")
    file.write("\nThis will add another line.")
    file.write("\nThis will add another new line.")
    
# Excercise 5: Write multiple Lines
lines = ["Line1\n","Line2\n","Line3\n"]

with open(textfile, "w") as file:
    file.writelines(lines)