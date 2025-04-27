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

Biomes = {
    "Windy": {"Chance": 500, "Amplify": 3},
    "Snowy": {"Chance": 600, "Amplify": 3},
    "Rainy": {"Chance": 750, "Amplify": 4},
    "Sandstorm": {"Chance": 3000, "Amplify": 4},
    "Hell": {"Chance": 6666, "Amplify": 6},
    "Starfall": {"Chance": 7500, "Amplify": 5},
    "Corruption": {"Chance": 9000, "Amplify": 5},
    "Null": {"Chance": 10100, "Amplify": 1000},
    "Glitched": {"Chance": 30000, "Amplify": 1}, # allows every biome's native aura to be amplified + some auras exclusive to glitch
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
    # 10
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
    # 100
    "★": {
        "rarity": 100,
        "display": fg("★" + "                    ", 213),
        "description": "★",
        "amplify": ['Glitched',False]
    },
    "Rage": {
        "rarity": 128,
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
    "Gilded": {
        "rarity": 500,
        "display": fg("Gilded" + "                    ", 172),
        "description": "Thats a shiny one!",
        "amplify": ['Sandstorm',True]
    },
    "Ink": {
        "rarity": 700,
        "display": fg("Ink" + "                    ", 250),
        "description": "Paint all Black",
        "amplify": ['NONE',True]
    },
    "Jackpot": {
        "rarity": 777,
        "display": fg("Jackpot" + "                    ", 226),
        "description": "Thats such a tremendous prize!",
        "amplify": ['Sandstorm',True]
    },
    "Sapphire": {
        "rarity": 800,
        "display": fg("Sapphire" + "                    ", 110),
        "description": "Gem of a azure hue",
        "amplify": ['NONE',True]
    },
    "Aquamarine": {
        "rarity": 900,
        "display": fg("Aquamarine" + "                    ", 81),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
     "Wind": {
        "rarity": 900,
        "display": fg("Wind" + "                    ", 87),
        "description": "The wind is hovering around you",
        "amplify": ['Windy',True]
    },

    # 1,000
    "★★": {
        "rarity": 1000,
        "display": fg("★ ★" + "                    ", 213),
        "description": "★ ★",
        "amplify": ['Glitched',False]
    },
    "Diaboli": {
        "rarity": 1004,
        "display": fg("Diaboli" + "                    ", 126),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Precious": {
        "rarity": 1024,
        "display": fg("Precious" + "                    ", 45),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Glock": {
        "rarity": 1700,
        "display": fg("Glock" + "                    ", 249),
        "description": "What do you mean by aura??? its just a Glock-17!",
        "amplify": ['NONE',True]
    },
    "Magnetic": {
        "rarity": 2048,
        "display": fg("Magnetic" + "                    ", 91),
        "description": "Its surrounded by powerful magnetic force",
        "amplify": ['NONE',True]
    },
    "Ash": {
        "rarity": 2300,
        "display": fg("Ash" + "                    ", 7),
        "description": "Everything that is destroyed goes back to ashes",
        "amplify": ['NONE',True]
    },
    "Glacier": {
        "rarity": 2304,
        "display": fg("Glacier" + "                    ", 81),
        "description": "a cold spirit",
        "amplify": ['Snowy',True]
    },
    "Fault": {
        "rarity": 3000,
        "display": (fg("FAULT", 10) + "                    "),
        "description": "a heterogeneous substance",
        "amplify": ['Glitched',False]
    },
    "Player": {
        "rarity": 3000,
        "display": ("Player" + "                    "),
        "description": "a heterogeneous substance",
        "amplify": ['NONE',True]
    },
    "Siderium": {
        "rarity": 4096,
        "display": (fg("Side", 220) + fg("reum", 170) + "                    "),
        "description": "A trail of broken stars",
        "amplify": ['NONE',True]
    },
    "Bleeding": {
        "rarity": 4444,
        "display": (fg("Bleeding", 88) + "                    "),
        "description": "Endlessly oozing blood... Hey, you sure alright?",
        "amplify": ['NONE',True]
    },
    "Solar": {
        "rarity": 5000,
        "display": fg("Solar" + "                    ", 222),
        "description": "It was made with Sunshine by an Unknown being on a bright day.",
        "amplify": ['NONE',True]
    },
    "Lunar": {
        "rarity": 5000,
        "display": fg("Lunar" + "                    ", 111),
        "description": "It was made with Moonlight by an Unknown being on a clear night.",
        "amplify": ['NONE',True]
    },
    "Flushed": {
        "rarity": 6900,
        "display": (fg("Flushed", 220) + "                    "),
        "description": "flushed",
        "amplify": ['NONE',True]
    },
    "Hazard": {
        "rarity": 7000,
        "display": (fg("Hazard", 177) + "                    "),
        "description": "This is a constant destruction of life",
        "amplify": ['Corrupted',True]
    },
    "Quartz": {
        "rarity": 8000,
        "display": (fg("Quartz", 183) + "                    "),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Lost Soul": {
        "rarity": 8200,
        "display": (fg("Lost Soul", 74) + "                    "),
        "description": "Empty",
        "amplify": ['NONE',True]
    },

    # 10,000 - Unique
    "★★★": {
        "rarity": 10000,
        "display": fg("★ ★ ★" + "                    ", 213),
        "description": "★ ★ ★",
        "amplify": ['Glitched',False]
    },
    "Undead": {
        "rarity": 12000,
        "display": (fg("Undead", 22) + "                    "),
        "description": "failed to die...",
        "amplify": ['Hell',True]
    },
    "Corrosive": {
        "rarity": 12000,
        "display": (fg("Corrosive", 128) + "                    "),
        "description": "failed to die...",
        "amplify": ['Corruption',True]
    },
    "Rage:Heated": {
        "rarity": 12800,
        "display": fg("Rage:Heated" + "                    ", 202),
        "description": "furious emotions",
        "amplify": ['NONE',True]
    },
    "Ink:LEAK": {
        "rarity": 14000,
        "display": fg("Ink : Leak" + "                    ", 250),
        "description": "Paint all Black",
        "amplify": ['NONE',True]
    },
    "Powered": {
        "rarity": 16384,
        "display": fg("Powered" + "                    ", 255),
        "description": "I feel like I've become more powerful!",
        "amplify": ['NONE',True]
    },
    "Aquatic": {
        "rarity": 40000,
        "display": fg("Aquatic" + "                    ", 69),
        "description": "It represents the flow of water",
        "amplify": ['NONE',True]
    },
    "Starlight": {
        "rarity": 50000,
        "display": fg("STARLIGHT" + "                    ", 117),
        "description": "This starlight with mysterious powers infused will follow you persistently, illuminating the path.",
        "amplify": ['Starfall',True]
    },
    "Star Rider": {
        "rarity": 50000,
        "display": fg("Star Rider" + "                    ", 227),
        "description": "A little friend who will join you on a wonderful trip",
        "amplify": ['Starfall',True]
    },
    "Flushed : Lobotomy": {
        "rarity": 69000,
        "display": (fg("Flushed : Lobotomy", 46) + "                    "),
        "description": "fire in the hole!!!",
        "amplify": ['NONE',True]
    },
    "Hazard : Rays": {
        "rarity": 70000,
        "display": (fg("Hazard : Rays", 105) + "                    "),
        "description": "This is a constant destruction of life",
        "amplify": ['Corrupted',True]
    },
    "Nautilus": {
        "rarity": 70000,
        "display": (fg("Nautilus", 63) + "                    "),
        "description": "A small shout resounding from the depths of the abyss..",
        "amplify": ['NONE',True]
    },
    "Permafrost": {
        "rarity": 73500,
        "display": (fg("Permafrost", 159) + "                    "),
        "description": "A small shout resounding from the depths of the abyss..",
        "amplify": ['Snowy',True]
    },
    "Stormal": {
        "rarity": 90000,
        "display": (fg("Stormal", 249) + "                    "),
        "description": "An enormous storm raging around you.",
        "amplify": ['Windy',True]
    },

    # 100,000 - Legendary
    "Exotic": {
        "rarity": 99999,
        "display": fg("E",196) + fg("x",220) + fg("o",226) + fg("t",154) + fg("i",120) + fg("c",87) + "                    ",
        "description": "Nobody knows where it originates from, and how old it is.",
        "amplify": ['NONE',True]
    },
    "Diaboli : Void": {
        "rarity": 100400,
        "display": fg("Diaboli : Void" + "                    ", 55),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Undead : Devil": {
        "rarity": 120000,
        "display": (fg("Undead : Devil", 203) + "                    "),
        "description": "silly tiny demon",
        "amplify": ['Hell',True]
    },
    "Comet": {
        "rarity": 120000,
        "display": (fg("COMET", 159) + "                    "),
        "description": "People believe that it has the capabilities to make wishes come true.",
        "amplify": ['Starfall',True]
    },
    "Jade": {
        "rarity": 120000,
        "display": (fg("Jade", 29) + "                    "),
        "description": "Where did it go?",
        "amplify": ['NONE',True]
    },
    "Spectre": {
        "rarity": 140000,
        "display": (fg("Spectre", 67) + "                    "),
        "description": "Where did it go?",
        "amplify": ['NONE',True]
    },
    "Jazz": {
        "rarity": 160000,
        "display": (fg("Jazz", 215) + "                    "),
        "description": "Jazz, a romance born in improvisation, where free melodies whisper the language of love.",
        "amplify": ['NONE',True]
    },
    "Aether": {
        "rarity": 180000,
        "display": (fg("Aether", 194) + "                    "),
        "description": "Mysterious matter believed to act as a medium for transmitting light The exact use is unknown.",
        "amplify": ['NONE',True]
    },
    "Bounded": {
        "rarity": 200000,
        "display": fg("BOUNDED" + "                    ", 17),
        "description": "It's too dangerous. Although it was sealed by an Ancient Power hundreds of thousands of years ago, its consciousness appears to be alive",
        "amplify": ['NONE',True]
    },
    "Celestial": {
        "rarity": 350000,
        "display": fg("Celestial" + "                    ", 219),
        "description": "An Individual with a sacredness that seems to have descended from heaven is havering around and delivering words of blessing.",
        "amplify": ['NONE',True]
    },
    "Kyawthuite": {
        "rarity": 850000,
        "display": fg("Kyawthuite" + "                    ", 129),
        "description": "once in a thousand years, in the deepest part of the forest...",
        "amplify": ['NONE',True]
    },

    # 1,000,000 - Mythic
    "Arcane": {
        "rarity": 1000000,
        "display": fg("Arcane" + "                    ", 117),
        "description": "A spell found in the ruins of an ancient civilization.",
        "amplify": ['NONE',True]
    },
    "Magnetic : Reverse Polarity": {
        "rarity": 1024000,
        "display": fg("Magnetic : Reverse Polarity" + "                    ", 127),
        "description": "A collection of strong energies with inverted directions of acting polarities, which are not described magnetically.",
        "amplify": ['NONE',True]
    },
    "Undefined": {
        "rarity": 1111000,
        "display": fg("[Undefined]" + "                    ", 250),
        "description": "It's too dark in here...",
        "amplify": ['Null',True]
    },
    "Rage : Brawler": {
        "rarity": 1280000,
        "display": fg("Rage : Brawler" + "                    ", 196),
        "description": "flame of emotions",
        "amplify": ['NONE',True]
    },
    "Astral": {
        "rarity": 133600,
        "display": fg("Astral" + "                    ", 135),
        "description": "In the distant expanse of space, tiny stars emitting faint light come together to form a unified existence.",
        "amplify": ['Corruption',True]
    },
    "Cosmos": {
        "rarity": 1520000,
        "display": fg("Cosmos" + "                    ", 183),
        "description": "A galactic warrior who fought in the ancient space war. Countless years have passed since the war, but the scars of war still remains on its body.",
        "amplify": ['NONE',True]
    },
    "Gravitational": {
        "rarity": 2000000,
        "display": fg("Gravitational" + "                    ", 69),
        "description": "The irregularities of gravity incomprehensible to humans. It is thought to stem from the same material comprising the mysterious Great Attractor.",
        "amplify": ['NONE',True]
    },
    "Bounded : Unbound": {
        "rarity": 2000000,
        "display": fg("BOUNDED : UNBOUND" + "                    ", 21),
        "description": "When news spread that this being had awoken, people trembled in fear.",
        "amplify": ['NONE',True]
    },
    "Virtual": {
        "rarity": 2500000,
        "display": fg("Virtual" + "                    ", 87),
        "description": "An advanced hologram device created by an unnamed civilization.",
        "amplify": ['NONE',True]
    },
    "Savior": {
        "rarity": 3200000,
        "display": fg("Savior" + "                    ", 207),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Savior": {
        "rarity": 3200000,
        "display": fg("Savior" + "                    ", 207),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Aquatic : Flame": {
        "rarity": 4000000,
        "display": fg("Aquatic : Flame" + "                    ", 208),
        "description": "It represents the flow of the flames",
        "amplify": ['NONE',True]
    },

    # 10,000,000 - Exalted
    "Glitched": {
        "rarity": 12210110,
        "display": (fg("G", 232) + fg("L", 250) + fg("I", 234) + fg("T", 250) + fg("C", 252) + fg("H", 245) + "                    "),
        "description": "WHAT ? NO, IT'S RIDICULOUS. IT SHOULDN'T HAPPEN",
        "amplify": ['Glitched',False]
    },
    "Stormal : Hurricane": {
        "rarity": 13500000,
        "display": (fg("Stormal : Hurricane", 249) + "                    "),
        "description": "An enormous storm raging around you.",
        "amplify": ['Windy',True]
    },
    "Arcane : Legacy": {
        "rarity": 1024000,
        "display": fg("Arcane : Legacy" + "                    ", 117),
        "description": "A spell found in the ruins of an ancient civilization. Maybe it was... too powerful.",
        "amplify": ['NONE',True]
    },
    "Chromatic": {
        "rarity": 20000000,
        "display": (fg("C", 196) + fg("H", 202) + fg("R", 226) + fg("O", 82) + fg("M", 48) + fg("A", 39) + fg("T", 99) + fg("I", 201) + fg("C", 196) + "                    "),
        "description": "Yes... Feel my unstoppable beats!",
        "amplify": ['NONE',True]
    },
    "Arcane : Dark": {
        "rarity": 1024000,
        "display": fg("Arcane : Dark" + "                    ", 93),
        "description": "A spell found in the ruins of an ancient civilization. This dreadful entity, no longer a mere spell, now is a sentient being",
        "amplify": ['NONE',True]
    },
    "Exotic : APEX": {
        "rarity": 49999500,
        "display": (fg("Exotic : APEX", 85) + "                    "),
        "description": "Maybe this is the source of the ancient being, that people were dying to know about?",
        "amplify": ['NONE',True]
    },


    # 99,999,999 - Glorious
    "Chromatic:Genesis": {
        "rarity": 99999999,
        "display": (fg("CHROMATIC : GENESIS", 153) + "                    "),
        "description": "WAKE UP FROM AWAY",
        "amplify": ['NONE',True]
    },
    "Oppression": {
        "rarity": 220000000,
        "display": (fg("O", 255) + fg("p", 249) + fg("p", 238) + fg("r", 255) + fg("e", 238) + fg("s", 245) + fg("s", 250) + fg("i", 238) + fg("o", 243) + fg("n", 247) + "                    "),
        "description": "... is this truly the end?",
        "amplify": ['Glitched',False]
    },
    "Exotic : VOID": {
        "rarity": 299999999,
        "display": (fg("Exotic : VOID", 165) + "                    "),
        "description": "Nobody knows where it originates from, and how old it is.",
        "amplify": ['NONE',True]
    },
    "Abyssal Hunter": {
        "rarity": 400000000,
        "display": (fg("ABYSSAL HUNTER", 27) + "                    "),
        "description": "An unknown hunter, slaughtering deep sea creatures mercilessly and roaming around the trenches.",
        "amplify": ['NONE',True]
    },
    # 1,000,000,000 - Transcendents
    "Pixelation": {
        "rarity": 1073741824,
        "display": (fg('▣ ', 196) + fg('P', 202) + fg('I', 226) + fg('X', 82) + fg('L', 48) + fg('E', 39) + fg('A', 99) + fg('T', 201) + fg('I', 201) + fg('O', 201) + fg('N', 201) + fg(' ▣', 199) + "                    "),
        "description": "“This description contains 0% lies and 1,000,000% TRUTH!”",
        "amplify": ['NONE',True]
    },
    "Luminosity": {
        "rarity": 1200000000,
        "display": (fg("[Luminosity]", 195) + "                    "),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
}


def format_chance(num) -> None:
    if num < 10:
        return f"{num:.3f}"
    elif num < 100:
        return f"{num:.2f}"
    elif num < 1000:
        return f"{num:,.1f}"
    else:
        return f"{num:,.0f}"

def show_aura_rarity(luck: float = 1.0, currentbiome: str = "None"):
    ListedAuras = {}

    for aura_name, aura_info in Auras.items():
        aura_copy = aura_info.copy()

        amplify_info = aura_copy.get('amplify', ['NONE', True])
        native_biome = amplify_info[0]
        biome_lock = amplify_info[1] if len(amplify_info) > 1 else True  # Default True if missing

        # check if biome-locked
        if not biome_lock:
            if currentbiome != native_biome:
                continue

        # if glitched biome
        if currentbiome == 'Glitched':
            if native_biome != 'NONE':
                biome_data = Biomes.get(native_biome)
                if biome_data and biome_data.get('Amplify'):
                    aura_copy['rarity'] /= biome_data['Amplify']

        # usual biome
        elif currentbiome != 'None':
            biome_data = Biomes.get(currentbiome)
            if biome_data and native_biome == currentbiome:
                if biome_data.get('Amplify'):
                    aura_copy['rarity'] /= biome_data['Amplify']

        ListedAuras[aura_name] = aura_copy

    # display
    for aura_name, aura_info in ListedAuras.items():
        rarity = aura_info["rarity"]
        actual_chance = rarity / luck

        if luck >= rarity:
            continue
        print(LINE)
        print("Rarity:", fg(f"1 / {int(rarity):,}", 81))
        print("Actual Chance:", fg(f"1 / {format_chance(actual_chance)}", 75))
        print(aura_info['display'])
        print(fg(f"Description: {aura_info['description']}", 244))
        print(LINE)
        time.sleep(0.1)


show_aura_rarity(1 * 1000 * 1000,'Glitched')
debugcolour()