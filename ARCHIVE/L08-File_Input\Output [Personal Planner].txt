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
            print(style.bred + "No task found." + style.RESET)
            return []
        else:
            for i in range(len(tasks)):
                if i == 0:
                    print(style.BOLD + tasks[i].strip() + style.RESET)
                else:
                    print(style.bblue +f"{i}" + style.RESET, f". {tasks[i]}".strip())
    return tasks

def marktask(fullpath : str) -> None:
    with open(fullpath, "r") as textfile:
        tasks = viewalltasks(fullpath)

    if len(tasks) == 1:
        print(style.bred + "No task found." + style.RESET)
        return []
    else:
        print(LINE)
        print(style.BOLD + "What task do you want to mark" + style.RESET)
        for i in range(len(tasks) - 1):
            print(style.bblue +f"{i+1}" + style.RESET, f". {tasks[i+1]}".strip())

        stop = 0
        while stop == 0:
            print(style.bcyan + "Please put a number from" + style.RESET, style.BOLD + f"1 to {len(tasks) - 1}" + style.RESET)
            mark = input("")
            if mark.isnumeric():
                if int(mark) > len(tasks) - 1:
                    print(style.bred + "EThe input is larger than the length of the list." + style.RESET)
                elif int(mark) < 1:
                    print(style.bred + "The input is smaller than 1" + style.RESET)
                else:
                    stop = 1
            else:
                print(style.bred + "The input is not a number." + style.RESET)
        
        taskindex = int(mark)
        if "[DONE]" in tasks[taskindex]:
            print(LINE)
            print(style.byellow + "This task is already done.")
        else:
            print(LINE)
            print(style.bgreen + "The task has been marked as done." + style.RESET)
            tasks[taskindex] = tasks[taskindex] + " [DONE]"

        with open(fullpath, "w") as taskfile:
            taskfile.writelines(tasks)

        
def deletetask(fullpath : str) -> None:
    with open(fullpath, "r") as textfile:
        tasks = viewalltasks(fullpath)

    if len(tasks) < 1:
        print(style.bred + "No task found." + style.RESET)
        return []
    else:
        print(LINE)
        print(style.BOLD + "What task do you want to remove" + style.RESET)
        for i in range(len(tasks) - 1):
            print(style.bblue +f"{i+1}" + style.RESET, f". {tasks[i+1]}".strip())

        stop = 0
        while stop == 0:
            print(style.bcyan + "Please put a number from" + style.RESET, style.BOLD + f"1 to {len(tasks) - 1}" + style.RESET)
            mark = input("")
            if mark.isnumeric():
                if int(mark) > len(tasks) - 1:
                    print(style.bred + "The input is larger than the length of the list." + style.RESET)
                elif int(mark) < 1:
                    print(style.bred + "The input is smaller than 1" + style.RESET)
                else:
                    stop = 1
            else:
                print(style.bred + "The input is not a number." + style.RESET)
    

    taskindex = int(mark)
    tasks[taskindex] = ""

    with open(fullpath, "w") as taskfile:
        taskfile.writelines(tasks)


def console():
    filename = "hi.txt"
    list = ["Create a new File","Add a new task","View all tasks","Mark a task","Delete a task","End the program"]
    num = 1

    stop = 0
    while stop == 0:
        num = 1
        print(style.BOLD + "What do you want to do? " + style.RESET)
        for item in list:
            print(style.bblue +f"{num}" + style.RESET, f". {item}")
            num += 1
        inputs = input("")
        if inputs.isnumeric():
            if int(inputs) > 6 or int(inputs) < 1:
                print(style.bred + "The input is not allowed.")
            else:
                # functions
                inp = int(inputs)
                if inp == 1:
                    createnewfile(os.path.join(textfile, "hi.txt"))
                elif inp == 2:
                    addnewtask(os.path.join(textfile, "hi.txt"))
                elif inp == 3:
                    viewalltasks(os.path.join(textfile, "hi.txt"))
                elif inp == 4:
                    marktask(os.path.join(textfile, "hi.txt"))
                elif inp == 5:
                    deletetask(os.path.join(textfile,"hi.txt"))
                elif inp == 6:
                    print("Ending program...")
                    stop = 1
        else:
            print(style.bred + "The input is not allowed.")



console()