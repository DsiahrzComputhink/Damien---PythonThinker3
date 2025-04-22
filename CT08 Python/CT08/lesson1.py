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

LINE = style.bgray + "-------------------------------" + style.RESET


import os
import time


FilePath = os.getcwd()
textfile = os.path.join(FilePath,"CT08 Python","ARCHIVE","Text Files","TOPIC-05 [ASCII]","[L12]-ASCII [hackmeifyoucan].txt")

if os.path.exists(textfile):
    print(style.bgreen + "[ {} ] Filepath Exists".format(textfile) + style.RESET)
else:
    print(style.bred + "[ {} ]  Filepath Does not Exist".format(textfile) + style.RESET)


    # character functions
def encryptChar(char: str, num: int):
    asciinum = ord(char) + num
    while asciinum > 126:
        asciinum %= 95
    return chr(asciinum)

def decryptChar(char: str, num: int):
    asciinum = ord(char) - num
    while asciinum < 32:
        asciinum += 95

    return chr(asciinum)

    # sentence functions
def encryptSentence(string: str, num: int):
    encryptedlist = ""
    for char in string:
        encryptedlist += encryptChar(char,num)
    return encryptedlist

def decryptSentence(string: str, num: int):
    decryptedlist = ""
    for char in string:
        decryptedlist += decryptChar(char,num)
    return decryptedlist

def encryptFile(content: str, num: int):
    encryptedlist = ""
    for line in content:
        encryptedsentence = encryptSentence(line, num)
        encryptedlist += f"\n{encryptedsentence}"
    return encryptedlist

def decryptFile(content: str, num: int):
    decryptedlist = ""
    for line in content:
        decryptedsentence = decryptSentence(line, num)
        decryptedlist += f"\n{decryptedsentence}"
    return decryptedlist

def BruteDecryptFile(content: str):
    num = 0.5
    d
    for i in range(95):
        decrypted = decryptFile(content,i)
        print(decrypted)
        print("[",style.bcyan + f"Shifted by {i}" + style.RESET,"]")
        time.sleep(num)
        if num > 0.25:
            num -= 0.01

with open(textfile, "r") as file:
    content = file.readlines()

def console():
    stop = 0
    while stop == 0:
        print(LINE)
        print("ENCRYPTION / DECRYPTION CONSOLE")
        print(LINE)
        print(style.bblue + "1" + style.RESET,"            ","Encrypt Sentence")
        print(style.bblue + "2" + style.RESET,"            ","Decrypt Sentence")
        print(style.bblue + "3" + style.RESET,"                ","Encrypt File")
        print(style.bblue + "4" + style.RESET,"                ","Decrypt File")
        print(style.bblue + "5" + style.RESET,"            ","Brute Force File")
        print(LINE)
        command = input("")
        if command.isnumeric():
            if int(command) == 1:
                print("Please input a sentence")
                print(LINE)
                sentence = input("")
                print(LINE)
                print("Please input a number to encrypt")
                print(LINE)
                number = input("")
                if number.isnumeric():
                    encrypted = encryptSentence(sentence,int(number))
                    print(LINE)
                    print(style.bpurple + "Decrypted Sentence:" + style.RESET,f"{sentence}")
                    print(style.bpurple + "Encrypted Sentence:" + style.RESET,f"{encrypted}")
                else:
                    print(style.bred + "Number is not numeric")
        else:
            print(style.bred + "Command does not exist")
        stop += 1

console()