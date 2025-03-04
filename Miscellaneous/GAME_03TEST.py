import random

words = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        ]
wordnumber = random.randint(0,len(words)-1)
def generatealgebra(word):


    

    x = Symbol(words[wordnumber])

    print(7*x + x + 1)
    # 2*x + 1
