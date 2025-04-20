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

import os
FilePath = os.getcwd()
# textfile = os.path.join(FilePath,"ARCHIVE","L07-File_Input\Output [example].txt")

# if os.path.exists(textfile):
#    print("hi")
      
minrange = 32
maxrange = 126


def encryptChar(char: str, num: int):
    asciinum = ord(char) + num
    print(asciinum)
    while asciinum > 126:
        print(asciinum)
        asciinum -= 126
    print(asciinum)

def decryptChar(char: str, num: int):
    asciinum = ord(char) - num
    print(asciinum)
    while asciinum < 32:
        print(asciinum)
        asciinum += 126
    print(asciinum)

string = "A"

encryptChar(string,942)
decryptChar(string,942)