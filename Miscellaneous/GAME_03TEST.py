import random
from sympy import Symbol

words = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        ]


def generatealgebra(word):

    wordnumber = random.randint(0,len(words)-1)


    symbol = Symbol(words[int(wordnumber)])
    return symbol

x = generatealgebra(words)
y = generatealgebra(words)

print(7*x + y + 1)
# 2*x + 1