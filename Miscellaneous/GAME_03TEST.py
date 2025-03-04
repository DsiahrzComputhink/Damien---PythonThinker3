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
min = 0
max = 10

words = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        ]


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


print(7*y + x + 1)
# 2*x + 1

ans = (5*x + 3)*(1-x)
print(ans)
# 6


def solveSimul():
    x = generatealgebra(words)
    y = generatealgebra(words)
    num1 = generaterandomnumber(min,max)
    num2 = generaterandomnumber(min,max)
    print(LINE)
    print(style.BOLD + "Simultaneous Equation" style.RESET)

solveSimul()