import random
from sympy import Symbol

words = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        ]


def generatealgebra(words : list):
    wordnumber = random.randint(0,len(words)-1)

    symbol = Symbol(words[int(wordnumber)])
    return symbol

x = generatealgebra(words)
y = generatealgebra(words)

print(7*y + x + 1)
# 2*x + 1

from sympy import *
expr = x**3 + x*y - x**2 - 2*y + y**3
res = expr.subs({x:1, y:2})
print(res)
# 6