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

LINE = style.bgray + "------------------------------" + style.RESET

import string
punctuation = string.punctuation
import os

FilePath = os.getcwd()
textfile = os.path.join(FilePath,"ARCHIVE","Text Files","encryptednote.txt")

with open(textfile,"r") as file:
    encrypted = file.read()

def lowercase(encrypted):
    print(style.bred + "WITH UPPER CASE" + style.RESET)
    print(encrypted)
    print(LINE)
    lowercase_encrypted = encrypted.lower()
    print(style.bgreen + "LOWERCASE" + style.RESET)
    print(lowercase_encrypted)
    print(LINE)
    return lowercase_encrypted

def removepunctuation(encrypted):
    print(style.bred + "WITH PUNCTUATION" + style.RESET)
    print(encrypted)
    print(LINE)
    for char in encrypted:
        if char in punctuation:
            encrypted.replace(f"{char}")
            
    print(style.bgreen + "WITHOUT PUNCTUATION" + style.RESET)
    print(LINE)


lowercase(encrypted)
removepunctuation(encrypted)