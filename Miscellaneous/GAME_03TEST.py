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

from sympy import Eq, solve
from sympy.abc import w, x, y, z

sol = solve([ Eq(2*w + x + 4*y + 3*z, 5),
              Eq(w - 2*x + 3*z, 3),
              Eq(3*w + 2*x - y + z, -1),
              Eq(4*x - 5*z, -3) ])
print(sol)
print({ s:sol[s].evalf() for s in sol })