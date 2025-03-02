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

# Class Grading System 
# grade all students based on their answers [done]
# calculate the average score for the class [done]
# identify the students with the highest score [done]
# display all results in an organized format

# learn how to use python dictionaries and functions for real world applications like student grading
# practice handling lists loops and conditional logic

answer_key = ["A","B","C","D"]

student_answers = {

    "john": ["A","B","C","D"],

    "jane": ["A","B","C","D"],

    "alice": ["A","B","C","D"],

    "bob": ["A","B","C","D"],
}

def gradeallstudents(student_answers: dict, answer_key: list) -> dict:
    quizscores = {}
    print("Grading all students...")
    for student, answers in student_answers.items():
        score = 0
        for i in range(len(answer_key)):
            if answers[i] == answer_key[i]:
                score += 1
        quizscores[f"{student}"] = score
    return(quizscores)
        

def calculateclassaverage(quizscores: dict) -> float:

    totalscore = 0
    for student, score in quizscores.items():
        totalscore += score
    average = totalscore / len(quizscores)

    print("The Class Average is")
    print(style.bcyan + f"{average}" + style.RESET)

    return average


def findhighestscorer(quizscores: dict) -> float:
    highestscorers = []
    highestvalue = max(quizscores.values())
    print("The Top Scorers are")
    for student, score in quizscores.items():
        if score == highestvalue:
            highestscorers.append(student)
            studentname = student.capitalize()
            print(style.bcyan + f"{studentname}" + style.RESET)

    return highestscorers


def displayresults(quizscores: dict):
    print(style.bblue + "Class Results:" + style.RESET)
    for student, score in quizscores.items():
        studentname = student.capitalize()
        print(f"{studentname} : {score}")


quizscores = gradeallstudents(student_answers,answer_key)
calculateclassaverage(quizscores)
findhighestscorer(quizscores)
displayresults(quizscores)

def program():
    stop = 0
    while stop == 0:
        time.sleep(3)
        print(style.bblue + "Class Grading System Menu")
        time.sleep(0.25)
        print(style.bcyan + "1" + style.RESET, "Grade All Students")
        time.sleep(0.25)
        print(style.bcyan + "2" + style.RESET, "Calcuate Class Average")
        time.sleep(0.25)
        print(style.bcyan + "3" + style.RESET, "Find Highest Scorer")
        time.sleep(0.25)
        print(style.bcyan + "4" + style.RESET, "Display All Results")
        time.sleep(0.25)
        print(style.bcyan + "5" + style.RESET, "Exit")
        time.sleep(0.25)
        command = input("")
        cmd = str(command)
        print(cmd)
        if cmd == "1":
            gradeallstudents(student_answers,answer_key)
        elif cmd == "2":
            calculateclassaverage(quizscores)
        elif cmd == "3":
            findhighestscorer(quizscores)
        elif cmd == "4":
            displayresults(quizscores)
        elif cmd == "5":
            print("Closing Program...")
            print(style.bblue + "Goodbye!" + style.RESET)
            stop += 1
        else:
            print(style.bred + "Not a Valid Command." + style.RESET)


program()