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

import time
import random
import os
FilePath = os.getcwd()
textfile = os.path.join(FilePath,"ARCHIVE","[MISC] Memory.txt")

if os.path.exists(textfile):
    print("{} exist".format(textfile))
else:
    print("{} Does not exist".format(textfile))

DefaultMemory = {"Lives":0, "Correct":0, "Wrong":0, "Round":0}
memory = {}


with open(textfile, "r") as file:
    content = file.read()

memory = eval(content)

LINE = style.black + "------------------------------" + style.RESET

if str(memory) == str("hi"):
    print("Yes") #debug test
else:
    print(LINE)
    print("NOTICE!")
    print(style.bred + "Your memory was corrupted." + style.RESET)
    print(style.bgray + "We have reset your memory for you." + style.RESET)
    print(LINE)
    with open(textfile, "w") as file:
        file.write(str(DefaultMemory))