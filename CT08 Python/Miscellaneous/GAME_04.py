import time
import random
import sys

# --- SOLS RNG CALCULATOR --- #
# Calculates the chances of you getting something

fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"
bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"
LINE = fg("------------------------------",235)

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

debugcolour()

Biomes = {
    "Windy": {"Chance": 500, "Amplify": 1.0},
    "Snowy": {"Chance": 600, "Amplify": 1.2},
    "Rainy": {"Chance": 750, "Amplify": 1.1},
    "Sandstorm": {"Chance": 3000, "Amplify": 1.5},
    "Hell": {"Chance": 6666, "Amplify": 2.0},
    "Starfall": {"Chance": 7500, "Amplify": 2.5},
    "Corruption": {"Chance": 9000, "Amplify": 2.8},
    "Null": {"Chance": 10100, "Amplify": 3.0},
    "Glitched": {"Chance": 30000, "Amplify": 5.0}, # allows every biome's native to appear
}

Auras = {
    "Common": {
        "rarity": 2,
        "display": fg("Common" + "                    ", 255),
        "description": "Very common thing",
        "amplify": ['NONE',True],
    },
    "Uncommon": {
        "rarity": 4,
        "display": ("Uncommon" + "                    "),
        "description": "super uncommon",
        "amplify": ['NONE',True]
    },
    "Good": {
        "rarity": 5,
        "display": fg("Good" + "                    ", 255),
        "description": "its super good",
        "amplify": ['NONE',True]
    },
    "Natural": {
        "rarity": 8,
        "display": fg("Natural" + "                    ", 120),
        "description": "very natural thing",
        "amplify": ['NONE',True]
    },

    "Rare": {
        "rarity": 16,
        "display": fg("Rare" + "                    ", 39),
        "description": "rare thing",
        "amplify": ['NONE',True]
    },
    "Divinus": {
        "rarity": 32,
        "display": fg("Divinus" + "                    ", 230),
        "description": "holy thing",
        "amplify": ['NONE',True]
    },
    "Crystallized": {
        "rarity": 64,
        "display": fg("Crystallized" + "                    ", 183),
        "description": "shiny thing",
        "amplify": ['NONE',True]
    },
    "Rage": {
        "rarity": 128,
        "display": fg("Rage" + "                    ", 160),
        "description": "flame of emotions",
        "amplify": ['NONE',True]
    },
        "Rage:Heated": {
        "rarity": 1280000,
        "display": fg("Rage" + "                    ", 160),
        "description": "flame of emotions",
        "amplify": ['NONE',True]
    },

    "Rage:Brawler": {
        "rarity": 12800,
        "display": fg("Rage" + "                    ", 160),
        "description": "flame of emotions",
        "amplify": ['NONE',True]
    },


    "Topaz": {
        "rarity": 150,
        "display": fg("Topaz" + "                    ", 137),
        "description": "Gem of a brown hue",
        "amplify": ['NONE',True]
    },
    "Ruby": {
        "rarity": 350,
        "display": fg("Ruby" + "                    ", 124),
        "description": "Gem of a brown hue",
        "amplify": ['NONE',True]
    },
    "Forbidden": {
        "rarity": 404,
        "display": fg("Forbidden" + "                    ", 111),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Emerald": {
        "rarity": 500,
        "display": fg("Emerald" + "                    ", 157),
        "description": "Gem of a green hue",
        "amplify": ['NONE',True]
    },

    "Chromatic": {
        "rarity": 20000000,
        "display": (fg("C", 196) + fg("H", 202) + fg("R", 226) + fg("O", 82) + fg("M", 48) + fg("A", 39) + fg("T", 99) + fg("I", 201) + fg("C", 196) + "                    "),
        "description": "Yes... Feel my unstoppable beats!"
    }
}


def format_chance(num):
    if num < 10:
        return f"{num:.3f}"
    elif num < 100:
        return f"{num:.2f}"
    elif num < 1000:
        return f"{num:,.1f}"
    else:
        return f"{num:,.0f}"

def show_aura_rarity(luck: float = 1.0):
    ListedAuras = {}
    for aura in Auras:
        if luck < Auras[aura]["rarity"]:
            ListedAuras[aura] = Auras[aura]
    for aura in ListedAuras:
        rarity = ListedAuras[aura]["rarity"]
        actual_chance = rarity / luck

        print(LINE)
        print("Rarity:", fg(f"1 / {rarity:,}", 81))
        print(f"Actual Chance:", fg(f"1 / {format_chance(actual_chance)}", 75))
        print(f"{ListedAuras[aura]['display']}")
        print(fg(f"Description: {ListedAuras[aura]['description']}", 244))
        print(LINE)

show_aura_rarity(11)
