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
LINE = style.bgray + "------------------------------" + style.RESET


print(style.bgray + "Placeholder" + style.RESET)
# Simple Text Colour ⬆

import os

FilePath = os.getcwd()
textfile = os.path.join(FilePath,"CT08 Python","ARCHIVE","Text Files","TOPIC-05 [ASCII]","[L11]-ASCII [Password Storage].txt")

if os.path.exists(textfile):
    print(style.bgreen + "[ {} ] Filepath Exists".format(textfile) + style.RESET)
else:
    print(style.bred + "[ {} ]  Filepath Does not Exist".format(textfile) + style.RESET)
# File Input\Output Dependency ⬆

def console():
    stop = 0
    while stop == 0:
        print(LINE)
        print("A TITLE")
        print(LINE)
        print(style.bblue + "1" + style.RESET,"                        ","a thing")
        print(style.bblue + "2" + style.RESET,"                  ","another thing")
        print(style.bblue + "3" + style.RESET,"                  ","Close Program")
        print(LINE)
        command = input("")
        if command.isnumeric():
            if int(command) == 1:
                print('hi')
            if int(command) == 2:
                print('hi')
            if int(command) == 3:
                print(style.bgreen + "Program closing..." + style.RESET)
                print("Goodbye!")
                stop += 1   
        else:
            print(style.bred + "Command does not exist" + style.RESET)

# Default Console Function ⬆

# --------------------------------------------------------------------
fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"
bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"

def debugcolour():

    def print_six(row, format, end="\n"):
        for col in range(6):
            color = row*6 + col - 2
            if color>=0:
                text = "{:3d}".format(color)
                print (format(text,color), end=" ")
            else:
                print(end="    ")   # four spaces
        print(end=end)

    for row in range(0, 43):
        print_six(row, fg, " ")
        print_six(row, bg)

debugcolour()
# Simple usage: print(fg("text", 160))
# AdvancedColour Function ⬆