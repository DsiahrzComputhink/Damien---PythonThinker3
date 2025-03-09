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

LINE = style.bgray + "------------------------------" + style.RESET

from sympy import Symbol
from sympy import *
min = 1
max = 10

# For some reason, h does not 
words = [
        '𝑎', '𝑏', '𝑐', '𝑑', '𝑒', '𝑓', '𝑔', '𝒉', '𝑖', '𝑗', '𝑘', '𝑙', '𝑚', '𝑛', '𝑜', '𝑝', '𝑞', '𝑟', '𝑠', '𝑡', '𝑢', '𝑣', '𝑤', '𝑥', '𝑦', '𝑧',
        ]

def answer(input: bool):
    if input == True:
        print("reward")
    elif input == False:
        print("punish")

def generatealgebra(words : list):
    wordnumber = random.randint(0,len(words)-1)

    symbol = Symbol(words[int(wordnumber)])
    return symbol

def generaterandomnumber(min,max):
    num = random.randint(min,max) # leave in positive.
    negative = random.randint(0,1)
    if negative == 1:
        num = num*(-1)
    return num

x = generatealgebra(words)
y = generatealgebra(words)


def solveSimul(x,y,xval,yval,num1,num2,num3,num4):
    equ1 = xval*num1 + yval*num2
    equ2 = yval*num3 + yval*num4
    print(LINE)
    print(style.BOLD + "Simultaneous Equation" + style.RESET)
    print(LINE)
    print(style.bcyan + "Solve the 2 equations." + style.RESET)
    print(f"({(num1*x + num2*y)} = {equ1})")
    print(f"({(num3*x + num4*y)} = {equ2})")
    print(xval)
    print(yval)
    print(style.bgray + "The letters go alphabetically, please be aware about it.")
    xvalans = input(style.bpurple + f"{x} = " + style.RESET)
    yvalans = input(style.bpurple + f"{y} = " + style.RESET)
    if xvalans.isnumeric() and yvalans.isnumeric():
        if xvalans != xval:
            return False
        elif xvalans == xval:
            if yvalans != yval:
                return False
            elif yvalans == yval:
                return True
    else:
        return False
    

def SimulQuestion():
    x = generatealgebra(words)
    y = generatealgebra(words)
    xval = generaterandomnumber(min,max)
    yval = generaterandomnumber(min,max)

    num1 = generaterandomnumber(min,max)
    num2 = generaterandomnumber(min,max)
    num3 = generaterandomnumber(min,max)
    num4 = generaterandomnumber(min,max)
    ans = solveSimul(x,y,xval,yval,num1,num2,num3,num4)
    if ans is False:
        print("FALSE")
    elif ans is True:
        print("TRUE")
    else:
        print(style.bred + "! Answer is neither False or True. !")

SimulQuestion()