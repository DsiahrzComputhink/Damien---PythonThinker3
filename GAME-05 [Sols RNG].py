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

    # Generic Colours
    primary = dblue
    secondary = bgray
    
    warning = dyellow
    error = dred
LINE = style.bgray + "--------------------------------" + style.RESET

fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"
bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"
LINE = fg("--------------------------------",232)
def debugcolour():

    def print_six(row, format, end="\n"):
        for col in range(6):
            color = row*6 + col - 2
            if color>=0:
                text = "{:3d}".format(color)
                print (format(text,color), end=" ")
            else:
                print(end="    ")   # four spaces
        print(end=end)

    for row in range(0, 43):
        print_six(row, fg, " ")
        print_six(row, bg)

import time
import random
import sys
import math
import os
import string

FilePath = os.getcwd()
textfile = os.path.join(FilePath,"CT08 Python","ARCHIVE","Text Files","GAME_05 Text Files","Auras.txt")

if os.path.exists(textfile):
    print(style.bgreen + "[ {} ] Filepath Exists".format(textfile) + style.RESET)
else:
    print(style.bred + "[ {} ]  Filepath Does not Exist".format(textfile) + style.RESET)

with open(textfile, "r") as file:
        content = file.read()
Auras = eval(content)

Tiers = [
    {"name": "BASIC", "range": (1, 999), "color": 250},
    {"name": "EPIC", "range": (1_000, 9_998), "color": 182},
    {"name": "UNIQUE", "range": (9_999, 99_998), "color": 179},
    {"name": "LEGENDARY", "range": (99_999, 999_998), "color": 220},
    {"name": "MYTHIC", "range": (999_999, 9_999_998), "color": 213},
    {"name": "EXALTED", "range": (9_999_999, 99_999_998), "color": 27},
    {"name": "GLORIOUS", "range": (99_999_999, 999_999_998), "color": 160},
    {"name": "TRANSCENDENT", "range": (999_999_999, float('inf')), "color": 153},
]

# Global Functions
def find_tier(rarity_value):
    for tier in Tiers:
        min_val, max_val = tier["range"]
        if min_val <= rarity_value <= max_val:
            return tier
    return None

def pick_aura(luck_multiplier: float = 1.0, auras: dict = None):
    auras = auras or Auras

    total_weight = 0
    weights = []

    for aura_name, aura_info in auras.items():
        rarity = aura_info["rarity"]
        if luck_multiplier > rarity:
            weight = 0
        else:
            weight = (1 / rarity) * luck_multiplier
        weights.append((aura_name, weight))
        total_weight += weight

    roll = random.uniform(0, total_weight)
    cumulative = 0
    for aura_name, weight in weights:
        cumulative += weight
        if roll <= cumulative:
            return aura_name, auras[aura_name]

    return "Common", auras["Common"]

def Roll(luck: float = 1.0, rollspeed: float = 1.0):
    roll_speed = 0.15 / rollspeed
    slowdown_rate = 1.1
    speed = roll_speed

    # Rolling animation
    for _ in range(10):
        _, temp_aura = pick_aura(luck)
        sys.stdout.write("\r" + fg(f"Rolling... {temp_aura['display']}                                                        ", random.randint(232, 255)))
        sys.stdout.flush()
        time.sleep(speed)
        speed *= slowdown_rate

    # Final roll
    _, selected_aura = pick_aura(luck)
    display_name = selected_aura["display"]

    sys.stdout.write("\r" + fg(f"You rolled {display_name} !                                              ", random.randint(232, 255)))
    sys.stdout.flush()
    sys.stdout.write("\r" + fg(f"You rolled {display_name} !", random.randint(232, 255)))
    sys.stdout.flush()
    print(f"\n")

    # Update inventory using display
    if display_name in InventoryAuras:
        InventoryAuras[display_name] += 1
    else:
        InventoryAuras[display_name] = 1

def craft(recipe: dict):
    requirement = 0
    completion = 0
    Incomplete = {}
    display = recipe["display"]
    unallowed = ["display","luck","rollspeed","type"]
    for item in recipe:
        if item not in unallowed:
            requirement += 1
            if item in InventoryAuras:
                if InventoryAuras[item] >= recipe[item]:
                    completion += 1
                else:
                    Incomplete[item] = f"{InventoryAuras[item]} / {recipe[item]}"
            else:
                Incomplete[item] = f"{0} / {f"{recipe[item]:,}"}"


    if requirement == completion:
        print(f"You've {fg("Sucessfully",82)} crafted {recipe['display']}!")

        for item in recipe:
            if item not in unallowed:
                InventoryAuras[item] -= recipe[item]

        if "type" in recipe and recipe["type"].lower() == "gauntlet":
            if display in InventoryGauntlets:
                InventoryGauntlets[display] += 1
            else:
                InventoryGauntlets[display] = 1

        if display in InventoryAuras:
            InventoryAuras[display] += 1
        else:
            InventoryAuras[display] = 1
    else:
        inventory(Incomplete, f"{fg(f"Not enough Resources",160)} for {recipe['display']}")

def inventory(inventory : dict,name: str) -> None:
    print(LINE)
    print(f"{name}")
    print(LINE)
    remove = []
    for name, count in inventory.items():
        if count == 0:
            remove.append(name)
        else:
            print(f"{name} : {count}")
    print(LINE)
    for item in remove:
        del inventory[item]

def equip(recipe: str):
    global luck, rollspeed
    if recipe["display"] in InventoryGauntlets:
        if "luck" in recipe:
            luck = recipe["luck"]
            if "rollspeed" in recipe:
                rollspeed = recipe["rollspeed"]
                print(f"{fg('Equipped', 248)} {recipe['display']} — {fg("Luck",84)} = {luck:0.2f}, {fg("Rollspeed",117)} = {rollspeed:0.2f}")
    else:
        print(f"{fg('You do not have', 160)} {recipe['display']}")


# Global Variables
InventoryAuras = {}
InventoryGauntlets = {}
Recipes = {}

# Auras
Recipes["Eclipse"] = {
    Auras["Solar"]["display"]: 1, 
    Auras["Lunar"]["display"]: 1, 
    "display": f"{fg('Ecl', 215)}{fg('i',246)}{fg('pse',19)} {fg('[UNIQUE CRAFTED]',179)}",
    "type": "Aura"
}

Recipes["Matrix : Steampunk"] = {
    Auras["Gilded"]["display"]: 100000, 
    Auras["Powered"]["display"]: 6000, 
    Auras["Magnetic : Reverse Polarity"]["display"]: 375, 
    Auras["Virtual"]["display"]: 175, 
    Auras["Zeus"]["display"]: 10, 
    Auras["Hypervolt"]["display"]: 50, 
    Auras["Matrix"]["display"]: 9, 
    "display": f"{fg('MATRIX : STEAMPUNK', 216)} {fg('[GLORIOUS CRAFTED]',160)}",
    "type": "Aura"
}

# Gauntlets
Recipes["Gear Basing"] = {
    Auras["Rare"]["display"]: 1,
    Auras["Good"]["display"]: 1, 
    Auras["Uncommon"]["display"]: 1, 
    Auras["Common"]["display"]: 1,
    "display": f"{fg("[T0]",159)} {fg("Gear Basing", 245)}",
    "luck": 1.0,
    "rollspeed": 1.0,
    "type": "Gauntlet"
}

Recipes["Luck Glove"] = {
    Recipes["Gear Basing"]["display"]: 1,
    Auras["Rare"]["display"]: 3,
    Auras["Divinus"]["display"]: 2,
    Auras["Crystallized"]["display"]: 1, 
    "display": f"{fg("[T1]",153)} {fg("Luck Glove", 83)}",
    "luck": 1.5,
    "rollspeed": 1.1,
    "type": "Gauntlet"
}

Recipes["Lunar Device"] = {
    Recipes["Gear Basing"]["display"]: 1,
    Auras["Rare"]["display"]: 1,
    Auras["Divinus"]["display"]: 1, 
    Auras["Lunar"]["display"]: 1, 
    "display": f"{fg("[T1]",153)} {fg("Lunar Device", 147)}",
    "luck": 1,
    "rollspeed": 1.15,
    "type": "Gauntlet"
}

Recipes["Solar Device"] = {
    Recipes["Gear Basing"]["display"]: 1,
    Auras["Rare"]["display"]: 1,
    Auras["Divinus"]["display"]: 1, 
    Auras["Solar"]["display"]: 1, 
    "display": f"{fg("[T1]",153)} {fg("Solar Device", 222)}",
    "luck": 1.50,
    "rollspeed": 1,
    "type": "Gauntlet"
}

Recipes["Eclipse Device"] = {
    Recipes["Solar Device"]["display"]: 1, 
    Recipes["Lunar Device"]["display"]: 1, 
    Recipes["Eclipse"]["display"]: 1, 
    "display": f"{fg("[T2]",117)} {fg('Eclip', 215)}{fg('se De',246)}{fg('vice',19)}",
    "luck": 1.50,
    "rollspeed": 1.15,
    "type": "Gauntlet"
}

Recipes["Exo Gauntlet"] = {
    Recipes["Gear Basing"]["display"]: 3,
    Auras["Gilded"]["display"]: 3,
    Auras["Precious"]["display"]: 2,
    Auras["Magnetic"]["display"]: 2,
    Auras["Siderium"]["display"]: 1,
    Auras["Undead"]["display"]: 1, 
    Auras["Exotic"]["display"]: 1,
    "display": f"{fg("[T3]",81)} {fg("Exo Gauntlet", 117)}",
    "luck": 1.00 + 1.00,
    "rollspeed": 1.00 + 0.20,
    "type": "Gauntlet"
}

Recipes["Windstorm Device"] = {
    Recipes["Gear Basing"]["display"]: 5,
    Auras["Wind"]["display"]: 25,
    Auras["Precious"]["display"]: 12,
    Auras["Siderium"]["display"]: 4,
    Auras["Aquatic"]["display"]: 1, 
    Auras["Stormal"]["display"]: 1,
    "display": f"{fg("[T3]",81)} {fg("Windstorm Device",37)}",
    "luck": 1.00 + 1.15,
    "rollspeed": 1.00 + 0.30,
    "type": "Gauntlet"
}

Recipes["Subzero Device"] = {
    Recipes["Gear Basing"]["display"]: 5,
    Auras["Crystallized"]["display"]: 600,
    Auras["Glacier"]["display"]: 60,
    Auras["Precious"]["display"]: 40,
    Auras["Magnetic"]["display"]: 20, 
    Auras["Siderium"]["display"]: 10, 
    Auras["Aquatic"]["display"]: 2, 
    Auras["Permafrost"]["display"]: 2,
    "display": f"{fg("[T4]",75)} {fg("Subzero Device", 110)}",
    "luck": 1.00 + 1.50,
    "rollspeed": 1.00 + 0.30,
    "type": "Gauntlet"
}

Recipes["Galactic Device"] = {
    Recipes["Gear Basing"]["display"]: 25,
    Auras["Solar"]["display"]: 15,
    Auras["Lunar"]["display"]: 15,
    Recipes["Eclipse Device"]["display"]: 1,
    Auras["Sapphire"]["display"]: 100,
    Auras["Magnetic"]["display"]: 62, 
    Auras["Diaboli"]["display"]: 80, 
    Auras["Comet"]["display"]: 3, 
    Auras["Galaxy"]["display"]: 1,
    "display": f"{fg("[T5]",69)} {fg("Galactic Device", 134)}",
    "luck": 1.00 + 2.50,
    "rollspeed": 1.00 + 0.30,
    "type": "Gauntlet"
}

Recipes["Volcanic Device"] = {
    Recipes["Gear Basing"]["display"]: 6,
    Recipes["Solar Device"]["display"]: 1,
    Recipes["Windstorm Device"]["display"]: 1,
    Auras["Rage"]["display"]: 1000,
    Auras["Diaboli"]["display"]: 140, 
    Auras["Bleeding"]["display"]: 55, 
    Auras["Rage : Heated"]["display"]: 10, 
    Auras["Hades"]["display"]: 1,
    "display": f"{fg("[T5]",69)} {fg("Volcanic Device", 202)}",
    "luck": 1.00 + 2.90,
    "rollspeed": 1.00 + 0.35,
    "type": "Gauntlet"
}

Recipes["Exoflex Device"] = {
    Recipes["Exo Gauntlet"]["display"]: 1,
    Auras["Rare"]["display"]: 30000,
    Auras["Forbidden"]["display"]: 2000,
    Auras["Aquamarine"]["display"]: 1000,
    Auras["Siderium"]["display"]: 350,
    Auras["Undead"]["display"]: 37,
    Auras["Starlight"]["display"]: 80, 
    Auras["Exotic"]["display"]: 50, 
    Auras["Jade"]["display"]: 5, 
    Auras["Arcane"]["display"]: 3,
    "display": f"{fg("[T6]",63)} {fg("Exo", 210)}{fg("fle", 216)}{fg("x D", 222)}{fg("evi", 157)}{fg("ce", 159)}",
    "luck": 1.00 + 3.40,
    "rollspeed": 1.00 + 0.35,
    "type": "Gauntlet"
}

Recipes["Hologrammer"] = {
    Recipes["Exo Gauntlet"]["display"]: 1,
    Auras["Forbidden"]["display"]: 4000,
    Auras["Diaboli"]["display"]: 1645,
    Auras["Magnetic"]["display"]: 830,
    Auras["Player"]["display"]: 600,
    Auras["Rage : Heated"]["display"]: 145,
    Auras["Starlight"]["display"]: 80,
    Auras["Comet"]["display"]: 30, 
    Auras["Twilight"]["display"]: 3,
    Auras["Kyawthuite"]["display"]: 2, 
    Auras["Magnetic : Reverse Polarity"]["display"]: 2,
    Auras["Virtual"]["display"]: 2,
    "display": f"{fg("[T6]",63)} {fg("Hologrammer",117)}",
    "luck": 1.00 + 3.95,
    "rollspeed": 1.00 + 0.35,
    "type": "Gauntlet"
}

Recipes["Ragnaröker"] = {
    Auras["Rage"]["display"]: 23000,
    Auras["Diaboli"]["display"]: 3200,
    Auras["Ash"]["display"]: 1450,
    Auras["Siderium"]["display"]: 800,
    Auras["Lost Soul"]["display"]: 300,
    Auras["Rage : Heated"]["display"]: 230, 
    Auras["Lunar"]["display"]: 175,
    Auras["Solar"]["display"]: 175, 
    Auras["Star Rider"]["display"]: 75,
    Auras["Poseidon"]["display"]: 3,
    Auras["Zeus"]["display"]: 3,
    Auras["Hades"]["display"]: 3,
    "display": f"{fg("[T7]",99)} {fg("Ragnaröker",161)}",
    "luck": 1.00 + 4.55,
    "rollspeed": 1.00 + 0.40,
    "type": "Gauntlet"
}

Recipes["Darkshader"] = {
    Auras["Forbidden"]["display"]: 37000,
    Auras["Ink"]["display"]: 22000, 
    Auras["Diaboli"]["display"]: 14800, 
    Auras["Bleeding"]["display"]: 3350, 
    Auras["Hazard"]["display"]: 2250, 
    Auras["Lunar"]["display"]: 2700, 
    Auras["Ink:LEAK"]["display"]: 1150,
    Auras["Undefined"]["display"]: 20, 
    Auras["Twilight"]["display"]: 5,
    Auras["Arcane : Dark"]["display"]: 1,
    "display": f"{fg("[T8]",141)} {fg("Darkshader", 99)}",
    "luck": 5.0,
    "rollspeed": 5.0,
    "type": "Gauntlet"
}

Recipes["Gravitational Device"] = {
    Recipes["Gear Basing"]["display"]: 15,
    Auras["Diaboli"]["display"]: 152, 
    Auras["Precious"]["display"]: 152, 
    Auras["Magnetic"]["display"]: 75, 
    Auras["Siderium"]["display"]: 31, 
    Auras["Nautilus"]["display"]: 5,
    Auras["Exotic"]["display"]: 5, 
    Auras["Bounded"]["display"]: 3,
    Auras["Gravitational"]["display"]: 1,
    "display": f"{fg("[T8]",141)} {fg("Gravitational Device", 63)}",
    "luck": 5.0,
    "rollspeed": 5.0,
    "type": "Gauntlet"
}

Recipes["Starshaper"] = {
    Recipes["Gravitational Device"]["display"]: 1,
    Recipes["Galactic Device"]["display"]: 1,
    Recipes["Solar Device"]["display"]: 15,
    Recipes["Lunar Device"]["display"]: 15,
    Auras["Magnetic"]["display"]: 5600,
    Auras["Siderium"]["display"]: 2700,
    Auras["Lunar"]["display"]: 1500, 
    Auras["Solar"]["display"]: 1500,
    Auras["Star Rider"]["display"]: 200, 
    Auras["Comet"]["display"]: 90,
    Auras["Gravitational"]["display"]: 6,
    Auras["Galaxy"]["display"]: 3,
    Auras["Hypervolt"]["display"]: 3,
    Auras["Starscourge"]["display"]: 2,
    "display": f"{fg("[T8]",141)} {fg("Starshaper", 219)}",
    "luck": 1.00 + 4.55,
    "rollspeed": 1.00 + 0.40,
    "type": "Gauntlet"
}

Recipes["Neuralyzer"] = {
    Recipes["Hologrammer"]["display"]: 1,
    Auras["Lost Soul"]["display"]: 2500,
    Auras["Flushed"]["display"]: 2000,
    Auras["Starlight"]["display"]: 250, 
    Auras["Exotic"]["display"]: 400,
    Auras["Bounded : Unbound"]["display"]: 20, 
    Auras["Twilight"]["display"]: 10,
    Auras["Virtual"]["display"]: 18,
    Auras["Origin"]["display"]: 7,
    Auras["Chromatic"]["display"]: 2,
    "display": f"{fg("[T9]",177)} {fg("Ne", 216)}{fg("ur", 222)}{fg("al", 157)}{fg("yz", 159)}{fg("er", 183)}",
    "luck": 1.00 + 4.55,
    "rollspeed": 1.00 + 0.40,
    "type": "Gauntlet"
}

Recipes["Pole Light Core Device"] = {
    Auras["Magnetic"]["display"]: 9000,
    Auras["Siderium"]["display"]: 7250,
    Auras["Solar"]["display"]: 5000, 
    Auras["Permafrost"]["display"]: 300,
    Auras["Jade"]["display"]: 100, 
    Auras["Magnetic : Reverse Polarity"]["display"]: 25,
    Auras["Origin"]["display"]: 5,
    Auras["Hypervolt"]["display"]: 4,
    Auras["Sirius"]["display"]: 3,
    Auras["Blizzard"]["display"]: 3,
    "display": f"{fg("[T9]",177)} {fg("Pole", 153)} {fg("Light", 147)} {fg("Core", 141)} {fg("Device", 177)}",
    "luck": 1.00 + 4.55,
    "rollspeed": 1.00 + 0.40,
    "type": "Gauntlet"
}


# LUCK = ((1 + Basic Luck) * Bonus Roll + Special Buff) * VIP

luck = 1
rollspeed = math.inf

for i in range(13):
    for i in range(100):
        Roll(luck,rollspeed)
    luck *= 2.5

for i in range(20):
    craft(Recipes["Gear Basing"])


inventory(InventoryAuras, fg("Inventory", 220))
debugcolour()

for recipe in Recipes:
    craft(Recipes[recipe])

for recipe in Recipes:
    print(Recipes[recipe]["display"])

equip(Recipes["Exo Gauntlet"])
for i in range(10):
    Roll(luck,rollspeed)

#TIERS FOR GEAR: 1-153 2-117 3-81 4-75 5-69 6-63 7-99 8-141 9-177


    # DATA [wip]
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
textfile = os.path.join(FilePath,"CT08 Python","ARCHIVE","Text Files","GAME_05 Text Files","Data.txt")

if os.path.exists(textfile):
    print(style.bgreen + "[ {} ] Filepath Exists".format(textfile) + style.RESET)
else:
    print(style.bred + "[ {} ]  Filepath Does not Exist".format(textfile) + style.RESET)

with open(textfile, "r") as file:
        Data = file.read()
Data = eval(content)

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