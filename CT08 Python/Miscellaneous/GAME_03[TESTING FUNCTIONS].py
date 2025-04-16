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


LINE = style.bgray + "------------------------------" + style.RESET

    # dependencies
import time
import random
from sympy import Symbol
from sympy import *

    # constants
min = 1
max = 10

    # global functions
words = [
        '𝑎', '𝑏', '𝑐', '𝑑', '𝑒', '𝑓', '𝑔', '𝒉', '𝑖', '𝑗', '𝑘', '𝑙', '𝑚', '𝑛', '𝑝', '𝑞', '𝑟', '𝑠', '𝑡', '𝑢', '𝑣', '𝑤', '𝑥', '𝑦', '𝑧',
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

def turnnumberintopositive(number):
    if int(number) < 0:
        posnumber = number*-1
        return posnumber
    else:
        return number

def solveSimul(x,y,xval,yval,num1,num2,num3,num4):
    equ1 = xval*num1 + yval*num2
    equ2 = yval*num3 + yval*num4
    print(LINE)
    print(style.BOLD + "Simultaneous Equation" + style.RESET)
    print(LINE)
    print(style.bcyan + "Solve the 2 equations." + style.RESET)
    print(f"({(num1*x + num2*y)} = {equ1})")
    print(f"({(num3*x + num4*y)} = {equ2})")
    print(style.bgray + "The question is asking for the value" + style.RESET)
    xvalans = input(style.bpurple + f"{x} = " + style.RESET)
    yvalans = input(style.bpurple + f"{y} = " + style.RESET)
    print("")
    if str(xvalans) != str(xval):
        return False
    elif str(xvalans) == str(xval):
        if str(yvalans) != str(yval):
            return False
        elif str(yvalans) == str(yval):
            return True
    
def AlgebraicExpansion(x,y):
    print(LINE)
    print(style.BOLD + "Algebraic Expansion" + style.RESET)
    print(LINE)
    print(style.bcyan + "Simplify this Equation" + style.RESET)
    difficulty = random.randint(1,3)
    if difficulty == 1:
        num1 = generaterandomnumber(min,max)
        num2 = generaterandomnumber(min,max)
        num3 = generaterandomnumber(min,max)
        xval = num2 * num1
        yval = num3 * num1
        print(f"{num1}({(num2*x)} + {(num3*y)})")
        xvalans = input(style.bpurple + f"{x} = " + style.RESET)
        yvalans = input(style.bpurple + f"{y} = " + style.RESET)
        print(style.bgray + "The question is asking for the coefficent" + style.RESET)
        if str(xvalans) != str(xval):
            return False
        elif str(xvalans) == str(xval):
            if str(yvalans) != str(yval):
                return False
            elif str(yvalans) == str(yval):
                return True
    elif difficulty == 2:
        num1 = generaterandomnumber(min,max)
        num2 = generaterandomnumber(min,max)
        num3 = generaterandomnumber(min,max)
        z = generatealgebra(words)
        xval = num2
        yval = num3
        print(f"{num1*z}({(num2*x)} + {(num3*y)})")
        xvalans = input(style.bpurple + f"{z*x} = " + style.RESET)
        yvalans = input(style.bpurple + f"{z*y} = " + style.RESET)
        print(style.bgray + "The question is asking for the coefficent" + style.RESET)
        if str(xvalans) != str(xval):
            return False
        elif str(xvalans) == str(xval):
            if str(yvalans) != str(yval):
                return False
            elif str(yvalans) == str(yval):
                return True
    elif difficulty == 3:
        num1 = generaterandomnumber(min,max)
        num2 = generaterandomnumber(min,max)
        num3 = generaterandomnumber(min,max)
        w = generatealgebra(words)
        num4 = generaterandomnumber(min,max)
        z = generatealgebra(words)
        xval = num2
        yval = num3
        print(f"{num4*w}({num1*z}({(num2*x)} + {(num3*y)}))")
        xvalans = input(style.bpurple + f"{w*x*z} = " + style.RESET)
        yvalans = input(style.bpurple + f"{w*y*z} = " + style.RESET)
        print(style.bgray + "The question is asking for the coefficent" + style.RESET)
        if str(xvalans) != str(xval):
            return False
        elif str(xvalans) == str(xval):
            if str(yvalans) != str(yval):
                return False
            elif str(yvalans) == str(yval):
                return True

def AlgebraicFactorization(x,y):
    print(LINE)
    print(style.BOLD + "Algebraic Factorization" + style.RESET)
    print(LINE)
    print(style.bcyan + "Simplify this Equation" + style.RESET)
    print(style.bgray + "Factorize the Equation first, and then find the coefficent of the variable." + style.RESET)
    difficulty = random.randint(1,3)
    if difficulty == 1:
        num1 = generaterandomnumber(min,max)
        num2 = generaterandomnumber(min,max)
        num3 = generaterandomnumber(min,max)
        xval = num1
        yval = num2
        print(f"{num1*num2*x + num1*num3*y}")
        print(style.bgray + "The question is asking for the coefficent" + style.RESET)
        xvalans = input(style.bpurple + f"{x} = " + style.RESET)
        yvalans = input(style.bpurple + f"{y} = " + style.RESET)
        xvalanspos = turnnumberintopositive(int(xvalanspos))
        yvalanspos = turnnumberintopositive(int(yvalanspos))
        xvalpos = turnnumberintopositive(xval)
        yvalpos = turnnumberintopositive(yval)
        if str(xvalanspos) != str(xvalpos):
            return False
        elif str(xvalanspos) == str(xvalpos):
            if str(yvalanspos) != str(yvalpos):
                return False
            elif str(yvalanspos) == str(yvalpos):
                return True
    elif difficulty == 2:
        num1 = generaterandomnumber(min,max)
        num2 = generaterandomnumber(min,max)
        num3 = generaterandomnumber(min,max)
        z = generatealgebra(words)
        xval = num2
        yval = num3
        print(f"{num1*num2*x*z + num1*num3*y*z}")
        print(style.bgray + "The question is asking for the coefficent" + style.RESET)
        xvalans = input(style.bpurple + f"{x} = " + style.RESET)
        yvalans = input(style.bpurple + f"{y} = " + style.RESET)
        xvalanspos = turnnumberintopositive(xvalans)
        yvalanspos = turnnumberintopositive(yvalans)
        xvalpos = turnnumberintopositive(xval)
        yvalpos = turnnumberintopositive(yval)
        if str(xvalanspos) != str(xvalpos):
            return False
        elif str(xvalanspos) == str(xvalpos):
            if str(yvalanspos) != str(yvalpos):
                return False
            elif str(yvalanspos) == str(yvalpos):
                return True
            
def QuadraticEquation(x,R1,R2,axval,bxval):
    # R1 and R2 are integers, axval and bxval are coefficents
    ax = x*axval
    bx = x*bxval
    # (ax,R1)(bx,R2) = ax*bx + (ax*R2 + bx*R1) + R1*R2
    print(f"({ax})")
    print(ax*bx)
    print((ax*R2)+(bx*R1))
    print(R1*R2)
    
x = generatealgebra(words)
x1val = generaterandomnumber(min,max)
x2val = generaterandomnumber(min,max)

QuadraticEquation(x,4,2,x1val,x2val)
    # local functions
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
        print(style.bred + "! Answer is neither False or True. !" + style.RESET)