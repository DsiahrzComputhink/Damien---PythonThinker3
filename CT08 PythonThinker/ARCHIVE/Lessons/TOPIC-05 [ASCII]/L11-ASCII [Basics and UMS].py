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
LINE = style.bgray + "----------------------------------" + style.RESET

import time
import string
import random
import os

# random.choice([List,List2]) chooses a random element from the list.

# -- RANGES
    # Uppercase Leters: 65 - 90
    # Lowercase Letters: 97 - 122
    # Digits: 48 - 57
    # Symbols: 33 - 47, 58 - 64, 91 - 96
    # Space: 32

    # RANGE is 32 - 126


# ASCII User Management System (UMS)

# Must DO:
# * Create new users with automatically generated strong passwords.
# * Update existing passwords by verifiying the current one.
# * View usernames and their masked passwords.
# * Access all features through a interactive menu system.

# side note, this might be the basis of life for all data-based games
FilePath = os.getcwd()
textfile = os.path.join(FilePath,"CT08 PythonThinker","ARCHIVE","Text Files","TOPIC-05 [ASCII]","[L11]-ASCII [Password Storage].txt")

if os.path.exists(textfile):
    print(style.bgreen + "[ {} ] Filepath Exists".format(textfile) + style.RESET)
else:
    print(style.bred + "[ {} ]  Filepath Does not Exist".format(textfile) + style.RESET)

def loaddatabase(textfile):
    with open(textfile, "r") as file:
        filedata = file.read()
    datadictionary = eval(filedata)
    return datadictionary

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

def createusername(username: str, length: int = 12):
    if len(username) < 3:
        print(style.bred + f"Username can not be less than 3 letters long" + style.RESET)
    else:
        spaces = 0
        for i in username:
                    if i == " ":
                        spaces += 1
        if spaces > 0:
            print(style.byellow + "Username can not contain spaces" + style.RESET)

        if username in userDatabase:
            print(style.bred + f"There is already a user named {username}" + style.RESET)
            return None
        else:
            password = generatepassword(length)
            userDatabase[f"{username}"] = {}
            userDatabase[f"{username}"]['PASSWORD'] = password

            userDatabase[f"{username}"]['USEDPASSWORDS'] = [password] # usedpasswords is a list
            userDatabase[f"{username}"]['PERMS'] = 'CLIENT'

            print(LINE)
            print(style.bblue + "Welcome" + style.RESET, f"{username}.")
            print(style.bblue + "Your Password is:" + style.RESET, f"{password}.")
            return True

def updatepassword(username: str):
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
                                    print(style.byellow + "Sorry, this password has been used before. Create a different one." + style.RESET)
                                else:
                                    stop = 1
                        

            
        userDatabase[f"{username}"]['USEDPASSWORDS'].append(newpassword) # only happens after the new password is strong enough
        userDatabase[f"{username}"]['PASSWORD'] = newpassword
        stop == 0
    else:
        print(style.bred + "Username does not exist in database." + style.RESET)

def login():
    loginusername = input(style.bcyan + "Username: " + style.RESET)
    if loginusername in userDatabase:
        loginpassword = input(style.bcyan + "Password: " + style.RESET)
        if loginpassword == userDatabase[f"{loginusername}"]['PASSWORD']:
            print(style.bblue + f"You are now logged into {loginusername}" + style.RESET)
            return loginusername
        else:
            print(style.bred + "Invalid Password." + style.RESET)
            return None
    else:
        print(style.bred + "Username not found" + style.RESET)
        return None
        
def viewdatabase(userdb: dict,admin: bool) -> None:
    print(LINE)
    print(style.bgreen + "User Database" + style.RESET)
    print(LINE)
    if admin == False:
        for user in userdb:
            password = userdb[f"{user}"]['PASSWORD']
            rank = userdb[f"{user}"]['PERMS']
            print(f"{user}:","[")
            print("    ",style.bred + "Permissions:" + style.RESET,f"{rank}")
            print("    ",style.bcyan + "Password:" + style.RESET,f"{'#' * len(password)}")
            print("    ",style.byellow + "Used Passwords:" + style.RESET,"[")
            for usedpassword in userdb[f"{user}"]['USEDPASSWORDS']:
                print("    ","    ",f"{'#' * len(usedpassword)}")
            print("    ","]")
            print("]")

    elif admin == True:
        for user in userdb:
            password = userdb[f"{user}"]['PASSWORD']
            rank = userdb[f"{user}"]['PERMS']
            print(f"{user}:","[")
            print("    ",style.bcyan + "Permissions:" + style.RESET,f"{rank}")
            print("    ",style.bcyan + "Password:" + style.RESET,f"{password}")
            print("    ",style.byellow + "Used Passwords:" + style.RESET,"[")
            for usedpassword in userdb[f"{user}"]['USEDPASSWORDS']:
                print("    ","    ",f"{usedpassword}")
            print("    ","]")
            print("]")

def savedatabase(userdb: dict) -> None:
    with open(textfile, "w") as file:
        file.write(str(userdb))

def permuser(client,user,userdb: dict,perms: string) -> None:
    # PERMS:
    # 0 - Client
    # 1 - Moderator
    # 2 - Administrator
    # 3 - Developer [Can only be given via Dsiahrz]
    if user in userDatabase:
        #---
        if userdb[f"{client}"]['PERMS'] == 'CLIENT':
            allow = 0
        elif userdb[f"{client}"]['PERMS'] == 'MODERATOR':
            allow = 1
        elif userdb[f"{client}"]['PERMS'] == 'ADMINISTRATOR':
            allow = 2
        elif userdb[f"{client}"]['PERMS'] == 'DEVELOPER':
            allow = 3
        #---
        if userdb[f"{user}"]['PERMS'] == 'CLIENT':
            editallow = 0
        elif userdb[f"{user}"]['PERMS'] == 'MODERATOR':
            editallow = 1
        elif userdb[f"{user}"]['PERMS'] == 'ADMINISTRATOR':
            editallow = 2

        if perms == 'CLIENT':
            if allow < 1:
                print(style.byellow + "You do not have the permissions to edit this user.")
            else:
                if editallow > allow:
                    print(style.byellow + "You do not have the permissions to edit this user.")
                else:
                    userdb[f"{user}"]['PERMS'] = 'CLIENT'
                    print(style.bgreen + "Sucessfully edited Permissions")
        if perms == 'MODERATOR':
            if allow < 1:
                print(style.byellow + "You do not have the permissions to edit this user.")
            else:
                if editallow > allow:
                    print(style.byellow + "You do not have the permissions to edit this user.")
                else:
                    userdb[f"{user}"]['PERMS'] = 'MODERATOR'
                    print(style.bgreen + "Sucessfully edited Permissions")
        if perms == 'ADMINISTRATOR':
            if allow < 1:
                print(style.byellow + "You do not have the permissions to edit this user.")
            else:
                if editallow >= allow:
                    print(style.byellow + "You do not have the permissions to edit this user.")
                else:
                    userdb[f"{user}"]['PERMS'] = 'ADMINISTRATOR'
                    print(style.bgreen + "Sucessfully edited Permissions")
    else:
        print(style.bred + "Username does not exist in database." + style.RESET)

def console():
    stop = 0
    signedin = 0
    commandconsole = 0
    while stop == 0:
        if signedin == 0:
            print(LINE)
            print("ASCII User Management System [UMS]")
            print(LINE)
            print(style.bblue + "1" + style.RESET,"                        ","Sign In")
            print(style.bblue + "2" + style.RESET,"                          ","Login")
            print(style.bblue + "3" + style.RESET,"                  ","Close Program")
            print(LINE)
            command = input("")
            if command.isnumeric():
                if int(command) == 1:
                    print(LINE)
                    username = input(style.bblue + "Input a Username: " + style.RESET)
                    allow = createusername(username)
                    if allow == True:
                        savedatabase(userDatabase)
                        signedin = 1
                    else:
                        time.sleep(1)
                if int(command) == 2:
                    username = login()
                    if username != None:
                        signedin = 1
                if int(command) == 3:
                    print(style.bgreen + "Program closing... Goodbye!" + style.RESET)
                    stop += 1
            else:
                print(style.bred + "Command does not exist" + style.RESET)
        elif signedin == 1:
            if commandconsole == 0:
                print(LINE)
                print("{:<13}{:>30}".format("Welcome", style.bblue + username + style.RESET))
                print(LINE)
                print(style.bblue + "1" + style.RESET,"                ","Change Password")
                print(style.bblue + "2" + style.RESET,"                  ","View Commands")
                print(style.bblue + "3" + style.RESET,"                       ","Sign Out")
                print(LINE)
                command = input("")
                if command.isnumeric():
                    if int(command) == 1:
                        updatepassword(username)
                        savedatabase(userDatabase)
                    if int(command) == 2:
                        commandconsole = 1
                    if int(command) == 3:
                        print(LINE)
                        print(style.byellow + "Signing Out..." + style.RESET)
                        signedin = 0
                        username = None
                else:
                    print(style.bred + "Command does not exist" + style.RESET)
            elif commandconsole == 1:
                        print(LINE)
                        print("{:<13}{:>30}".format("Console", style.bblue + f"{username} [{userDatabase[f"{username}"]['PERMS']}]" + style.RESET))
                        print(LINE)
                        print(style.bblue + "1" + style.RESET,"                  ","View Database")
                        print(style.bblue + "2" + style.RESET,"            "," Change Permissions")
                        print(style.bblue + "3" + style.RESET,"                   ","Exit Console")
                        print(LINE)
                        command = input("")
                        if command.isnumeric():
                            if int(command) == 1:
                                if userDatabase[f"{username}"]['PERMS'] == 'CLIENT':
                                    viewdatabase(userDatabase,False)
                                else:
                                    viewdatabase(userDatabase,True)
                                time.sleep(1)
                            if int(command) == 2:
                                print(LINE)
                                print(style.bblue + "Please type in a username")
                                print(LINE)
                                userNum = 0
                                for user in userDatabase:
                                    if userDatabase[f"{user}"]['PERMS'] == 'DEVELOPER':
                                        time.sleep(0.5 / int(len(userDatabase)))
                                        print("{:<13}{:>30}{}".format(style.bblue + f"{userNum}" + style.RESET, f"{user}",style.bcyan + f" [{userDatabase[f"{user}"]['PERMS']}]" + style.RESET))
                                        userNum += 1
                                    elif userDatabase[f"{user}"]['PERMS'] == 'ADMINISTRATOR':
                                        time.sleep(0.5 / int(len(userDatabase)))
                                        print("{:<13}{:>30}{}".format(style.bblue + f"{userNum}" + style.RESET, f"{user}",style.bred + f" [{userDatabase[f"{user}"]['PERMS']}]" + style.RESET))
                                        userNum += 1
                                    elif userDatabase[f"{user}"]['PERMS'] == 'MODERATOR':
                                        time.sleep(0.5 / int(len(userDatabase)))
                                        print("{:<13}{:>30}{}".format(style.bblue + f"{userNum}" + style.RESET, f"{user}",style.byellow + f" [{userDatabase[f"{user}"]['PERMS']}]" + style.RESET))
                                        userNum += 1
                                    else:
                                        time.sleep(0.5 / int(len(userDatabase)))
                                        print("{:<13}{:>30}{}".format(style.bblue + f"{userNum}" + style.RESET, f"{user}",style.bgreen + f" [{userDatabase[f"{user}"]['PERMS']}]" + style.RESET))
                                        userNum += 1
                                print(LINE)
                                usertarget = input("")
                                if usertarget in userDatabase:
                                    print(LINE)
                                    print(style.bblue + "Please type in a number")
                                    print(LINE)
                                    print("{:<13}{:>30}".format(style.bblue + "1" + style.RESET, "[CLIENT]"))
                                    print("{:<13}{:>30}".format(style.bblue + "2" + style.RESET, "[MODERATOR]"))
                                    print("{:<13}{:>30}".format(style.bblue + "3" + style.RESET, "[ADMINISTRATOR]"))
                                    print(LINE)
                                    permNum = input("")
                                    if permNum.isnumeric():
                                        if int(permNum) == 1:
                                            permuser(username,usertarget,userDatabase,'CLIENT')
                                            savedatabase(userDatabase)
                                        elif int(permNum) == 2:
                                            permuser(username,usertarget,userDatabase,'MODERATOR')
                                            savedatabase(userDatabase)
                                        elif int(permNum) == 3:
                                            permuser(username,usertarget,userDatabase,'ADMINISTRATOR')
                                            savedatabase(userDatabase)
                                    else:
                                        print(style.bred + "Command does not exist" + style.RESET)
                                else:
                                    print(style.bred + "Username does not exist in Database" + style.RESET)
                                time.sleep(1)
                            if int(command) == 3:
                                commandconsole = 0


userDatabase = loaddatabase(textfile)

console()