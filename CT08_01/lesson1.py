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

a = 0
e = 0
i = 0
o = 0
u = 0

space = 0
total = 0
nonvowel = 0
characters = 0

import os
FilePath = os.getcwd()
textfile = os.path.join(FilePath,"ARCHIVE","Text Files","sherlock.txt")
with open(textfile,"r") as file:
    lines = file.readlines()


List = []

for line in lines:
    line1 = line.strip()
    List.append(str(line1))

for line in List:
    for word in line:
        for letter in word:
            # find if its a vowel
            if letter == "a":
                a += 1
                characters += 1
            elif letter == "e":
                e += 1
                characters += 1
            elif letter == "i":
                i += 1
                characters += 1
            elif letter == "o":
                o += 1
                characters += 1
            elif letter == "u":
                u += 1
                characters += 1
            elif letter != " ":
                nonvowel += 1
                characters += 1
            else:
                space += 1
            total += 1
            

print("Final output:")
print("\n")
print("a: ",a)
print("e: ",e)
print("i: ",i)
print("o: ",o)
print("u: ",u)
print("Non vowels:", nonvowel)
print("Spaces: ", space)
print("Characters: ", characters)
print("Total Amount: ", total)