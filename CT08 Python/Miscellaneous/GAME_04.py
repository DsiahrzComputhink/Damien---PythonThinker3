import time
import random
import sys

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

Auras = {
    "Common": {
        "rarity": 2,
        "display": fg("Common" + "                    ", 255),
        "description": "Very common thing"
    },
    "Uncommon": {
        "rarity": 4,
        "display": ("Uncommon" + "                    "),
        "description": "super uncommon"
    },
    "Good": {
        "rarity": 5,
        "display": fg("Good" + "                    ", 255),
        "description": "its super good"
    },
    "Natural": {
        "rarity": 8,
        "display": fg("Natural" + "                    ", 120),
        "description": "very natural thing"
    },
    "Chromatic": {
        "rarity": 20,
        "display": (fg("C", 196) + fg("H", 202) + fg("R", 226) + fg("O", 82) + fg("M", 48) + fg("A", 39) + fg("T", 99) + fg("I", 201) + fg("C", 196) + "                    "),
        "description": "Yes... Feel my unstoppable beats!"
    }
}

def pick_aura(luck_multiplier : int = 1.0):
    total_weight = 0
    weights = []

    for aura_name, aura_info in Auras.items():
        rarity = aura_info["rarity"]
        if luck_multiplier > rarity:
            weight = 0
        else:
            weight = (1 / rarity) * luck_multiplier  # luck boost
        weights.append((aura_name, weight))
        total_weight += weight

    roll = random.uniform(0, total_weight)

    cumulative = 0
    for aura_name, weight in weights:
        cumulative += weight
        if roll <= cumulative:
            return Auras[aura_name]

    # fallback
    return Auras["Common"]

def roll_animation(luck : int = 1.0):
    aura_list = list(Auras.values())
    roll_speed = 0.1
    slowdown_rate = 1.1
    speed = roll_speed

    # Rolling animation
    for _ in range(10):
        temp_aura = pick_aura(luck)
        sys.stdout.write("\r" + fg(f"Rolling... {temp_aura['display']} ", random.randint(232, 255)))
        sys.stdout.flush()
        time.sleep(speed)
        speed *= slowdown_rate

    # Final result based on rarity
    selected_aura = pick_aura(luck)

    print("\n")
    print(LINE)
    print(fg(f"1 / {selected_aura['rarity']}", 80))
    print(f"Color: {selected_aura['display']}")
    print(fg(f"Description: {selected_aura['description']}", 244))
    print(LINE)

# LUCK = ((1 + Basic Luck) * Bonus Roll + Special Buff) * VIP
# Example usage
roll_animation(1000000)