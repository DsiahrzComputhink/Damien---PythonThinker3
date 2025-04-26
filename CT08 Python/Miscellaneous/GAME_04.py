import time
import random
import sys

fg = lambda text, color: "\33[38;5;" + str(color) + "m" + text + "\33[0m"
bg = lambda text, color: "\33[48;5;" + str(color) + "m" + text + "\33[0m"

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
        "display": fg("Common" + "     ", 255),
        "description": "Very common thing"
    },
    "Uncommon": {
        "rarity": 4,
        "display": (fg("C", 196) + fg("H", 202) + fg("R", 226) + fg("O", 82) + fg("M", 48) + fg("A", 39) + fg("T", 99) + fg("I", 201) + fg("C", 196) + "     "),
        "description": "Yes... Feel my unstoppable beats!"
    },
    "Good": {
        "rarity": 5,
        "display": fg("Common" + "     ", 255),
        "description": "Very common thing"
    },
    "Natural": {
        "rarity": 8,
        "display": (fg("C", 196) + fg("H", 202) + fg("R", 226) + fg("O", 82) + fg("M", 48) + fg("A", 39) + fg("T", 99) + fg("I", 201) + fg("C", 196) + "     "),
        "description": "Yes... Feel my unstoppable beats!"
    },
    "Chromatic": {
        "rarity": 20,
        "display": (fg("C", 196) + fg("H", 202) + fg("R", 226) + fg("O", 82) + fg("M", 48) + fg("A", 39) + fg("T", 99) + fg("I", 201) + fg("C", 196) + "     "),
        "description": "Yes... Feel my unstoppable beats!"
    }
}



print(fg("text",160))

def pick_aura():
    weighted_pool = []
    for aura in Auras.values():
        weighted_pool.extend([aura] * (100 // aura["rarity"]))
    return random.choice(weighted_pool)

def roll_animation():
    aura_list = list(Auras.values())
    roll_speed = 0.05
    slowdown_rate = 1.12
    speed = roll_speed

    # Rolling animation
    for _ in range(30):
        temp_aura = random.choice(aura_list)
        sys.stdout.write("\r" + fg(f"Rolling... {temp_aura['display']} ", random.randint(80, 250)))
        sys.stdout.flush()
        time.sleep(speed)
        speed *= slowdown_rate

    # Final result based on rarity
    selected_aura = pick_aura()

    print("\n")
    print("-" * 40)
    print(fg(f"1 / {selected_aura['rarity']}", 80))
    print(f"Color: {selected_aura['display']}")
    print(fg(f"Description: {selected_aura['description']}", 244))

# Example usage
roll_animation()