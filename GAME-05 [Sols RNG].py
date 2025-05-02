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

FilePath = os.getcwd()
textfile = os.path.join(FilePath,"CT08 Python","ARCHIVE","Text Files","GAME_05 Text Files","Auras.txt")

if os.path.exists(textfile):
    print(style.bgreen + "[ {} ] Filepath Exists".format(textfile) + style.RESET)
else:
    print(style.bred + "[ {} ]  Filepath Does not Exist".format(textfile) + style.RESET)

with open(textfile, "r") as file:
        content = file.read()
Auras = eval(content)
print(Auras)

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

Recipes["Neuralyzer"] = {
    Auras["Magnetic"]["display"]: 9000,
    Auras["Siderium"]["display"]: 7250,
    Auras["Solar"]["display"]: 5000, 
    Auras["Permafrost"]["display"]: 300,
    Auras["Jade"]["display"]: 100, 
    Auras["Magnetic : Reverse Polarity"]["display"]: 25,
    Auras["Origin"]["display"]: 18,
    Auras["Hypervolt"]["display"]: 7,
    Auras["Sirius"]["display"]: 2,
    Auras["Blizzard"]["display"]: 2,
    "display": f"{fg("[T9]",177)} {fg("Ne", 216)}{fg("ur", 222)}{fg("al", 157)}{fg("yz", 159)}{fg("er", 183)}",
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