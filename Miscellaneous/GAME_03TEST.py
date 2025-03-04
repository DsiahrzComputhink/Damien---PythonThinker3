import random
from sympy import Symbol
from sympy import *

words = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        ]


def generatealgebra(words : list):
    wordnumber = random.randint(0,len(words)-1)

    symbol = Symbol(words[int(wordnumber)])
    return symbol

def generaterandomnumber(log : int):
    num = random.randint(0,1*(log*10))
    negative = random.randint(0,1)
    if negative == 1:
        num*-1
    return num
    #log is for

x = generatealgebra(words)
y = generatealgebra(words)


print(7*y + x + 1)
# 2*x + 1

ans = expand((5*x + 3)*(1-x))
print(ans)
# 6