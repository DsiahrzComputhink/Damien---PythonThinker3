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
filepath = os.getcwd()

fullpath = os.path.join(filepath,"ARCHIVE","L07-File_Input\Output [example].txt")

if os.path.exists(fullpath):
    print("{} exist".format(fullpath))
else:
    print("{} does not exist".format(fullpath))