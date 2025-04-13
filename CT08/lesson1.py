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

import time
import string
import random

# random.choice([List,List2]) chooses a random element from the list.

# -- RANGES
    # Uppercase Leters: 65 - 90
    # Lowercase Letters: 97 - 122
    # Digits: 48 - 57
    # Symbols: 33 - 47, 58 - 64, 91 - 96


# ASCII User Management System (UMS)

# Must DO:
# * Create new users with automatically generated strong passwords.
# * Update existing passwords by verifiying the current one.
# * View usernames and their masked passwords.
# * Access all features through a interactive menu system.

def generatepassword(length: int = 12) -> str:
    if length < 12:
        print(style.bred + "Length must be more than 12 Characters." + style.RESET)

    password = ""
    for i in range(length):
        randomsection = random.randint(1,4)
        if randomsection == 1:
            password += random.choice(string.ascii_uppercase)
        elif randomsection == 2:
            password += random.choice(string.ascii_lowercase)
        elif randomsection == 3:
            password += random.choice(string.digits)
        elif randomsection == 4:
            password += random.choice(string.punctuation)
    return password

# Nested Dictionary
userDatabase = {}

def createusername(username: str):
    if username in userDatabase:
        print(style.bred + f"There is already a user named {username}" + style.RESET)
    else:
        password = generatepassword()
        userDatabase[f"{username}"] = {}
        userDatabase[f"{username}"]['PASSWORD'] = password

        userDatabase[f"{username}"]['USEDPASSWORDS'] = [password] # usedpasswords is a list
    return username

def updatepassword(username: str,password: str):
    if username in userDatabase:
        stop = 0
        while stop == 0:
            newpassword = input(style.bcyan + "Choose a new password: " + style.RESET)
            if len(newpassword) < 7:
                print(style.byellow + "Sorry, password must be 8 letters long.")
            else:
                number = 0
                upper = 0
                lower = 0
                spaces = 0
                for i in newpassword: # checking for number
                    if i == " ":
                        spaces += 1
                    if i.isnumeric():
                        number += 1
                    elif i.isupper():
                        upper += 1
                    elif i.islower():
                        lower += 1
                if number < 1:
                    print(style.byellow + "Sorry, password must contain at least 1 number" + style.RESET)
                else:
                    if upper < 1:
                        print(style.byellow + "Sorry, password must contain at least 1 uppercase letter" + style.RESET)
                    else:
                        if lower < 1: 
                            print(style.byellow + "Sorry, password must contain at least 1 lowercase letter" + style.RESET)
                        else:
                            if spaces >= 1: 
                                print(style.byellow + "Sorry, password cannot contain spaces" + style.RESET)
                            else:
                                if newpassword in userDatabase[f"{username}"]['USEDPASSWORDS']:
                                    print(style.byellow + "Sorry, this username has been used before. Create a different one." + style.RESET)
                                else:
                                    stop = 1
                        

            
        userDatabase[f"{username}"]['USEDPASSWORDS'].append(newpassword) # only happens after the new password is strong enough
        userDatabase[f"{username}"]['PASSWORD'] = newpassword
        print(userDatabase)
        stop == 0
    else:
        print(style.bred + "Username does not exist in database." + style.RESET)

def login():
    loginusername = input(style.bcyan + "Username: " + style.RESET)
    if loginusername in userDatabase:
        loginpassword = input(style.bcyan + "Password: " + style.RESET)
        if loginpassword == userDatabase[f"{loginusername}"]['PASSWORD']:
            print(style.bblue + f"You are now logged into {loginusername}" + style.RESET)
        else:
            print(style.bred + "Invalid Password." + style.RESET)
            return None
    else:
        print(style.bred + "Username not found" + style.RESET)
        return None
        
def viewdatabase(userdb: dict) -> None:
    for user in userdb:
        password = userdb[f"{user}"]['PASSWORD']
        print(f"{user}:","(")
        print("    ",style.bcyan + "Password:" + style.RESET,style.bpurple + f"{'*' * len(password)}")
        print("    ",style.byellow + "Used Passwords:" + style.RESET,"(")
        print("    ","    ","Password:",style.bpurple + f"{'*' * len(password)}")

        



createusername("username")
# updatepassword("username","password")
# login()
viewdatabase(userDatabase)
