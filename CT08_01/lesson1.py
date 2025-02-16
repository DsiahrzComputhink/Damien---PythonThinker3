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


# Check attendance percentage for astudent
# Notify low percentages for student
# Built a system menu to access functions

students = {
    "Alice": [True, False, True],
}



def createnewstudent(num):
    NAME = 1
    for i in range(num):
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
        
def ARCHIVE_attendance_percentage(student: str, students: dict) -> float:

    # if student is all, iterate through every student in dictionary
    if student == "all":
        for student in students:
            if student in students:
                attendancelist = students[student]
                TRUE = attendancelist.count(True)
                FALSE = attendancelist.count(False)
                Denom = len(attendancelist)
                p = round((TRUE/Denom) * 100,2)
                a = round((FALSE/Denom) * 100,2)
                print(style.bblue + f"{student}" + style.RESET,"is")
                print("Present",style.bgreen + f"{p}%" + style.RESET,"of the time")
                print("Absent",style.bgreen + f"{a}%" + style.RESET,"of the time")
                return round((TRUE/Denom) * 100,2)
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
            print(style.bblue + f"{student}" + style.RESET,"is")
            print("Present",style.bgreen + f"{p}%" + style.RESET,"of the time")
            print("Absent",style.bgreen + f"{a}%" + style.RESET,"of the time")
            return round((TRUE/Denom) * 100,2)
        else:
            print(style.dred + "STUDENT DOES NOT EXIST" + style.RESET)
        return 0.0
    return {}
    # if student is all, iterate through every student in dictionary
    for student in students:
        if student in students:
            attendancelist = students[student]
            TRUE = attendancelist.count(True)
            FALSE = attendancelist.count(False)
            Denom = len(attendancelist)
            p = round((TRUE/Denom) * 100,2)
            a = round((FALSE/Denom) * 100,2)
            print(style.bblue + f"{student}" + style.RESET,"is")
            print("Present",style.bgreen + f"{p}%" + style.RESET,"of the time")
            print("Absent",style.bgreen + f"{a}%" + style.RESET,"of the time")
            return round((TRUE/Denom) * 100,2)
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
        
# take_attendance(students)
# attendance_percentage("all",students)

def notify(students: dict, threshold: float) -> list:
    warning = []
    number_warning = 0
    for student in students.keys():
        percentage = silent_attendance_percentage(student, students)
        if percentage < threshold:
            warning.append(student)
            number_warning += 1
    if number_warning >= 1:
        print(style.bred + "! ALERT !" + style.RESET)
        print(style.bblue + "List of students to send warning" + style.RESET)
        for student in warning:
            print(student)
            percentage = silent_attendance_percentage(student, students)
            print("Present for only",style.bred + f"{percentage}%" + style.RESET,"of the time")
    else:
        print(style.dgreen + "No students below threshold." + style.RESET)
    
createnewstudent(10)
ARCHIVE_attendance_percentage(students)
notify(students,50.0)