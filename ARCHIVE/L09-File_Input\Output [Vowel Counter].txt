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
vowel = 0
words = 0
wordlines = 0
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

wordlines = len(lines)
wordend = 0
for line in List:
    for character in line:
            # find if its a vowel
            if character == "a" or character == "A":
                a += 1
                vowel += 1
                characters += 1
            elif character == "e" or character == "E":
                e += 1
                vowel += 1
                characters += 1
            elif character == "i" or character == "I":
                i += 1
                vowel += 1
                characters += 1
            elif character == "o" or character == "O":
                o += 1
                vowel += 1
                characters += 1
            elif character == "u" or character == "U":
                u += 1
                vowel += 1
                characters += 1
            elif character != " ":
                if wordend == 1:
                    words += 1
                    wordend = 0
                nonvowel += 1
                characters += 1
            else:
                wordend = 1
                space += 1
            total += 1
            
def results(variable,name: str,letter: str):
    print(style.bblue + f"{name}" + style.RESET,style.bwhite + f"{variable} {letter}," + style.RESET, style.bcyan + f"{(variable/total) * 100:.2f}%" + style.RESET,"of the Whole File")

def result(variable,name: str,letter: str):
    print(style.bblue + f"{name}" + style.RESET,style.bwhite + f"{variable} {letter}" + style.RESET)

print(style.bgray + "------------------" + style.RESET)
print(style.BOLD + "FINAL RESULTS" + style.RESET)
print(style.bgray + "------------------" + style.RESET)
# results
results(a,"Vowel 'a'","Letters")
results(e,"Vowel 'e'","Letters")
results(i,"Vowel 'i'","Letters")
results(o,"Vowel 'o'","Letters")
results(u,"Vowel 'u'","Letters")
print("")
results(vowel,"Vowels","Vowels")
results(nonvowel,"Non-Vowels","Non-Vowels")
print("")
results(space,"Spaces","Spaces")
result(words,"Words","Words")
result(wordlines,"Lines","Lines")
results(characters,"Characters","Characters")

import os
FileName = "L08-File_Input\Output [example].txt"
FilePath = os.getcwd()
textfile = os.path.join(FilePath,"ARCHIVE","Text Files")

def createnewfile(textfile: str) -> None:
    if os.path.exists(textfile):
        print()
    else:
        print(style.bblue + "\nCreating a new task file" + style.RESET)

        with open(textfile, "x") as taskfile:
            taskfile.write("Sherlock Holmes Text Analysis\n")
            taskfile.write("-----------------------------\n")
            taskfile.write("")
            taskfile.write(f"Total Characters: {total}\n")
            taskfile.write(f"Total Vowels: {vowel}\n")


createnewfile(os.path.join(textfile, "results.txt"))