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
import os
FileName = "L08-File_Input\Output [example].txt"
FilePath = os.getcwd()
textfile = os.path.join(FilePath,"ARCHIVE","Text Files")
print(textfile)
if os.path.exists(textfile):
    print(style.bgreen + "File connected." + style.RESET)
else:
    print(style.bred + "File does not exist." + style.RESET)

def createnewfile(textfile: str) -> None:
    # Creates a new task file if it does not already exist.
    # If the file exists, it notifies the user.
    if os.path.exists(textfile):
        print(LINE)
        print(style.byellow + "The file already exists." + style.byellow)
        print(LINE)
    else:
        print(style.bblue + "\nCreating a new task file" + style.RESET)

        with open(textfile, "x") as taskfile:
            taskfile.write("My Task List")


def addnewtask(fullpath : str) -> None:
    print(style.bblue + "Please input a task." + style.RESET)
    taskinput = input("")
    task = str(taskinput)

    with open(fullpath, "a") as taskfile:
        taskfile.write(f"\n{task}")

def viewalltasks(fullpath : str) -> None:
    with open(fullpath, "r") as textfile:
        tasks = textfile.readlines()
        if len(tasks) == 1:
            print(style.bred + "No task found.")
            return []
        else:
            for i in range(len(tasks)):
                if i == 0:
                    print(style.BOLD + tasks[i].strip() + style.RESET)
                else:
                    # if '[DONE]' in tasks[i].strip():
                    #     print(style.bblue +f"{i}" + style.RESET, f". {tasks[i]}".strip())
                    # else:
                    #     print('Apples not in string')
                    print(style.bblue +f"{i}" + style.RESET, f". {tasks[i]}".strip())

def marktask(fullpath : str) -> None:
    with open(fullpath, "r") as textfile:
        tasks = viewalltasks(os.path.join(textfile, "hi"))

        


createnewfile(os.path.join(textfile, "hi"))
# addnewtask(os.path.join(textfile, "hi"))
viewalltasks(os.path.join(textfile, "hi"))

