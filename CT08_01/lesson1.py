import random
import time

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


students = {
    #"Alice": [True, False, True],
}



def createnewstudent(num, num_attendance=5):
    NAME = 1
    for _ in range(num):
        attendance_list = []
        for _ in range(num_attendance):
            attendance_list.append(random.choice([True, True, False]))
        
        students[f"TEST{NAME}"] = attendance_list
        NAME += 1


def take_attendance(students: dict) -> dict:
    for student, attendance in students.items():
        print(student)
        while True:
            print("Is",style.bblue + f"{student}" + style.RESET,"Present?",style.dgreen + "Y" + style.RESET,"/",style.dred + "N" + style.RESET)
            attendance = input()
            attendance.lower()

            if attendance == "y":
                students[student].append(True)
                break
            elif attendance == "n":
                students[student].append(False)
                break
            else:
                print(style.bred + "INVALID" + style.RESET)
                print("Please only input",style.dgreen + "Y" + style.RESET,"or",style.dred + "N" + style.RESET)
                print("----------------------------")
        
def attendance_percentage(student: str, students: dict) -> float:
    # if student is all, iterate through every student in dictionary
    if student == "all":
        for student in students:
            attendancelist = students[student]
            TRUE = attendancelist.count(True)
            FALSE = attendancelist.count(False)
            Denom = len(attendancelist)
            p = round((TRUE/Denom) * 100,2)
            a = round((FALSE/Denom) * 100,2)
            if p == 100:
                COLOUR = style.bpurple
            elif p >= 99:
                COLOUR = style.bblue
            elif p >= 90:
                COLOUR = style.bcyan
            elif p > 75:
                COLOUR = style.dgreen
            elif p >= 50:
                COLOUR = style.bgreen
            elif p >= 30:
                COLOUR = style.byellow
            elif p <= 30:
                COLOUR = style.dred
            print(style.bgray + "-------------------------------" + style.RESET)
            print(style.bblue + f"{student}" + style.RESET,"is")
            print("Present",COLOUR + f"{p}%" + style.RESET,"of the time")
            print("Absent",COLOUR+ f"{a}%" + style.RESET,"of the time")
            time.sleep(5 / len(students))
        else:
            print(style.dred + "STUDENT DOES NOT EXIST" + style.RESET)
        return 0.0
    # -----------------------------------
    else:
        if student in students:
            attendancelist = students[student]
            TRUE = attendancelist.count(True)
            FALSE = attendancelist.count(False)
            Denom = len(attendancelist)
            p = round((TRUE/Denom) * 100,2)
            a = round((FALSE/Denom) * 100,2)
            if p == 100:
                COLOUR = style.bpurple
            elif p >= 99:
                COLOUR = style.bblue
            elif p >= 90:
                COLOUR = style.bcyan
            elif p >= 75:
                COLOUR = style.dgreen
            elif p >= 50:
                COLOUR = style.bgreen
            elif p >= 30:
                COLOUR = style.byellow
            elif p <= 30:
                COLOUR = style.dred
            print(style.bgray + "-------------------------------" + style.RESET)
            print(style.bblue + f"{student}" + style.RESET,"is")
            print("Present",COLOUR + f"{p}%" + style.RESET,"of the time")
            print("Absent",COLOUR + f"{a}%" + style.RESET,"of the time")
        else:
            print(style.dred + "STUDENT DOES NOT EXIST" + style.RESET)
        return 0.0

def silent_attendance_percentage(student: str, students: dict) -> float:
    if student in students:
        attendancelist = students[student]
        TRUE = attendancelist.count(True)
        Denom = len(attendancelist)
        return round((TRUE/Denom) * 100,2)
    return 0.0


def notify(students: dict, threshold: float) -> list:
    warning = []
    number_warning = 0
    for student in students.keys():
        percentage = silent_attendance_percentage(student, students)
        if percentage < threshold:
            warning.append(student)
            number_warning += 1
    if number_warning >= 1:

        print(style.bgray + "-------------------------------" + style.RESET)
        print(style.bred + "! ALERT !" + style.RESET)
        print(style.bblue + "List of students to send warning" + style.RESET)

        for student in warning:

            percentage = silent_attendance_percentage(student, students)
            print(style.bblue + f"{student}" + style.RESET,"is present for only",style.bred + f"{percentage}%" + style.RESET,"of the time")
    else:
        print(style.dgreen + "No students below threshold." + style.RESET)
    
createnewstudent(50,20)
attendance_percentage("all",students)
notify(students,50.0)

while True:
    print(style.bgray + "------------------------------------" + style.RESET)
    print(style.bblue + "1" + style.RESET, "Add new student")
    print(style.bblue + "2" + style.RESET, "Check attendance")