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
# grade all students based on their answers
# calculate the average score for the class
# identify the students with the highest score
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

    for student, answers in student_answers.items():
        score = 0
        for i in range(len(answer_key)):
            if answers[i] == answer_key[i]:
                score += 1
        quizscores[f"{student}"] = score
    return(quizscores)
        

def calculateclassaverage(student_answers: dict, answer_key: list) -> dict:
    average = 0

    total = 0
    correct = 0
    for student, answers in student_answers.items():
        for i in range(len(answer_key)):
            if answers[i] == answer_key[i]:
                correct += 1
            total += 1

gradeallstudents(student_answers,answer_key)