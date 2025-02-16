import random
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


# Add new attendance record to students
# Check attendance percentage for astudent
# Notify low percentages for student
# Built a system menu to access functions

students = {
    "Alice": [True, False, True],
}

NAME = 1
def createnewstudent():
    test = random.randint(1,4)
    if test > 1:
        a1 = True
    else:
        a1 = False
    test = random.randint(1,4)
    if test > 1:
        a2 = True
    else:
        a2 = False
    test = random.randint(1,4)
    if test > 1:
        a3 = True
    else:
        a3 = False
    students[f"TEST{NAME}"] = [a1,a2,a3]
    print(students)



def take_attendance(students: dict) -> dict:
    for _ in students():
        print("Is",style.bcyan + students(_) + style.RESET)
    return {}

take_attendance(students)