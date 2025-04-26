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

AuraColour = { # only meant for aura colour
    "Common":(fg("Common",255)),
    "Chromatic":(fg("C",196) + fg("H",202) + fg("R",226) + fg("O",82) + fg("M",48) + fg("A",39) + fg("T",99) + fg("I",201) + fg("C",196))
}

Auras = { # Main Variable
    "Common":[2,AuraColour["Common"],"Very common thing"],
    "Chromatic":[20,AuraColour["Chromatic"],"Yes.. Feel my unstoppable beats!"]
    }


print(fg("text",160))

for aura in Auras:
    for item in Auras[aura]:
        print(item)

def pick_aura():
    weighted_pool = []
    for aura_name, aura_info in Auras.items():
        rarity = aura_info[0]
        # More rare = fewer entries
        weighted_pool.extend([aura_name] * (100 // rarity))
    return random.choice(weighted_pool)

def roll_animation():
    aura_names = list(Auras.keys())
    roll_speed = 0.05
    slowdown_rate = 1.12
    speed = roll_speed

    selected = None

    # Rolling animation
    for _ in range(30):
        temp_pick = random.choice(aura_names)
        sys.stdout.write("\r" + fg(f"Rolling... {temp_pick} ", random.randint(80, 250)))
        sys.stdout.flush()
        time.sleep(speed)
        speed *= slowdown_rate

    # Final result based on rarity
    selected = pick_aura()

    print("\n")
    print(fg(f"🎉 You rolled: {selected}!", 82))
    print("-" * 40)
    aura = Auras[selected]
    print(fg(f"Power: {aura[0]}", 80))
    print(f"Color: {aura[1]}")
    print(fg(f"Description: {aura[2]}", 244))

# Example usage
roll_animation()