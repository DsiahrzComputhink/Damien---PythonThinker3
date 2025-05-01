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
LINE = style.bgray + "------------------------------" + style.RESET

import time
import random
import sys
import math

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
        "display": fg("Common", 255),
        "description": "Very common thing",
        "amplify": ['NONE',True],
    },
    "Uncommon": {
        "rarity": 4,
        "display":fg ("Uncommon",240),
        "description": "super uncommon",
        "amplify": ['NONE',True]
    },
    "Good": {
        "rarity": 5,
        "display": fg("Good", 255),
        "description": "its super good",
        "amplify": ['NONE',True]
    },
    "Natural": {
        "rarity": 8,
        "display": fg("Natural", 120),
        "description": "very natural thing",
        "amplify": ['NONE',True]
    },
    # 10
    "Rare": {
        "rarity": 16,
        "display": fg("Rare", 39),
        "description": "rare thing",
        "amplify": ['NONE',True]
    },
    "Divinus": {
        "rarity": 32,
        "display": fg("Divinus", 230),
        "description": "holy thing",
        "amplify": ['NONE',True]
    },
    "Crystallized": {
        "rarity": 64,
        "display": fg("Crystallized", 183),
        "description": "shiny thing",
        "amplify": ['NONE',True]
    },
    # 100
    "★": {
        "rarity": 100,
        "display": fg("★", 213),
        "description": "★",
        "amplify": ['Glitched',False]
    },
    "Rage": {
        "rarity": 128,
        "display": fg("Rage", 160),
        "description": "flame of emotions",
        "amplify": ['NONE',True]
    },
    "Topaz": {
        "rarity": 150,
        "display": fg("Topaz", 137),
        "description": "Gem of a brown hue",
        "amplify": ['NONE',True]
    },
    "Ruby": {
        "rarity": 350,
        "display": fg("Ruby", 124),
        "description": "Gem of a brown hue",
        "amplify": ['NONE',True]
    },
    "Forbidden": {
        "rarity": 404,
        "display": fg("Forbidden", 111),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Emerald": {
        "rarity": 500,
        "display": fg("Emerald", 157),
        "description": "Gem of a green hue",
        "amplify": ['NONE',True]
    },
    "Gilded": {
        "rarity": 500,
        "display": fg("Gilded", 172),
        "description": "Thats a shiny one!",
        "amplify": ['Sandstorm',True]
    },
    "Ink": {
        "rarity": 700,
        "display": fg("Ink", 250),
        "description": "Paint all Black",
        "amplify": ['NONE',True]
    },
    "Jackpot": {
        "rarity": 777,
        "display": fg("Jackpot", 226),
        "description": "Thats such a tremendous prize!",
        "amplify": ['Sandstorm',True]
    },
    "Sapphire": {
        "rarity": 800,
        "display": fg("Sapphire", 110),
        "description": "Gem of a azure hue",
        "amplify": ['NONE',True]
    },
    "Aquamarine": {
        "rarity": 900,
        "display": fg("Aquamarine", 81),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
     "Wind": {
        "rarity": 900,
        "display": fg("Wind", 87),
        "description": "The wind is hovering around you",
        "amplify": ['Windy',True]
    },

    # 1,000
    "★★": {
        "rarity": 1000,
        "display": fg("★ ★", 213),
        "description": "★ ★",
        "amplify": ['Glitched',False]
    },
    "Diaboli": {
        "rarity": 1004,
        "display": fg("Diaboli", 126),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Precious": {
        "rarity": 1024,
        "display": fg("Precious", 45),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Glock": {
        "rarity": 1700,
        "display": fg("Glock", 249),
        "description": "What do you mean by aura??? its just a Glock-17!",
        "amplify": ['NONE',True]
    },
    "Magnetic": {
        "rarity": 2048,
        "display": fg("Magnetic", 91),
        "description": "Its surrounded by powerful magnetic force",
        "amplify": ['NONE',True]
    },
    "Ash": {
        "rarity": 2300,
        "display": fg("Ash", 7),
        "description": "Everything that is destroyed goes back to ashes",
        "amplify": ['NONE',True]
    },
    "Glacier": {
        "rarity": 2304,
        "display": fg("Glacier", 81),
        "description": "a cold spirit",
        "amplify": ['Snowy',True]
    },
    "Fault": {
        "rarity": 3000,
        "display": (fg("FAULT", 10)),
        "description": "a heterogeneous substance",
        "amplify": ['Glitched',False]
    },
    "Player": {
        "rarity": 3000,
        "display": ("Player"),
        "description": "A true 8-bit move!",
        "amplify": ['NONE',True]
    },
    "Siderium": {
        "rarity": 4096,
        "display": (fg("Side", 220) + fg("reum", 170)),
        "description": "A trail of broken stars",
        "amplify": ['NONE',True]
    },
    "Bleeding": {
        "rarity": 4444,
        "display": (fg("Bleeding", 88)),
        "description": "Endlessly oozing blood... Hey, you sure alright?",
        "amplify": ['NONE',True]
    },
    "Solar": {
        "rarity": 5000,
        "display": fg("Solar", 222),
        "description": "It was made with Sunshine by an Unknown being on a bright day.",
        "amplify": ['NONE',True]
    },
    "Lunar": {
        "rarity": 5000,
        "display": fg("Lunar", 111),
        "description": "It was made with Moonlight by an Unknown being on a clear night.",
        "amplify": ['NONE',True]
    },
    "Flushed": {
        "rarity": 6900,
        "display": (fg("Flushed", 220)),
        "description": "flushed",
        "amplify": ['NONE',True]
    },
    "Hazard": {
        "rarity": 7000,
        "display": (fg("Hazard", 177)),
        "description": "This is a constant destruction of life",
        "amplify": ['Corrupted',True]
    },
    "Quartz": {
        "rarity": 8000,
        "display": (fg("Quartz", 183)),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Lost Soul": {
        "rarity": 8200,
        "display": (fg("Lost Soul", 74)),
        "description": "Empty",
        "amplify": ['NONE',True]
    },

    # 10,000 - Unique
    "★★★": {
        "rarity": 10000,
        "display": fg("★ ★ ★", 213),
        "description": "★ ★ ★",
        "amplify": ['Glitched',False]
    },
    "Undead": {
        "rarity": 12000,
        "display": (fg("Undead", 22)),
        "description": "failed to die...",
        "amplify": ['Hell',True]
    },
    "Corrosive": {
        "rarity": 12000,
        "display": (fg("Corrosive", 128)),
        "description": "failed to die...",
        "amplify": ['Corruption',True]
    },
    "Rage:Heated": {
        "rarity": 12800,
        "display": fg("Rage:Heated", 202),
        "description": "furious emotions",
        "amplify": ['NONE',True]
    },
    "Ink:LEAK": {
        "rarity": 14000,
        "display": fg("Ink : Leak", 250),
        "description": "Paint all Black",
        "amplify": ['NONE',True]
    },
    "Powered": {
        "rarity": 16384,
        "display": fg("Powered", 255),
        "description": "I feel like I've become more powerful!",
        "amplify": ['NONE',True]
    },
    "Aquatic": {
        "rarity": 40000,
        "display": fg("Aquatic", 69),
        "description": "It represents the flow of water",
        "amplify": ['NONE',True]
    },
    "Starlight": {
        "rarity": 50000,
        "display": fg("STARLIGHT", 117),
        "description": "This starlight with mysterious powers infused will follow you persistently, illuminating the path.",
        "amplify": ['Starfall',True]
    },
    "Star Rider": {
        "rarity": 50000,
        "display": fg("Star Rider", 227),
        "description": "A little friend who will join you on a wonderful trip",
        "amplify": ['Starfall',True]
    },
    "Flushed : Lobotomy": {
        "rarity": 69000,
        "display": (fg("Flushed : Lobotomy", 46)),
        "description": "fire in the hole!!!",
        "amplify": ['NONE',True]
    },
    "Hazard : Rays": {
        "rarity": 70000,
        "display": (fg("Hazard : Rays", 105)),
        "description": "This is a constant destruction of life",
        "amplify": ['Corrupted',True]
    },
    "Nautilus": {
        "rarity": 70000,
        "display": (fg("Nautilus", 63)),
        "description": "A small shout resounding from the depths of the abyss..",
        "amplify": ['NONE',True]
    },
    "Permafrost": {
        "rarity": 73500,
        "display": (fg("Permafrost", 159)),
        "description": "A small shout resounding from the depths of the abyss..",
        "amplify": ['Snowy',True]
    },
    "Stormal": {
        "rarity": 90000,
        "display": (fg("Stormal", 249)),
        "description": "An enormous storm raging around you.",
        "amplify": ['Windy',True]
    },

    # 100,000 - Legendary
    "Exotic": {
        "rarity": 99999,
        "display": fg("E",196) + fg("x",220) + fg("o",226) + fg("t",154) + fg("i",120) + fg("c",87),
        "description": "Nobody knows where it originates from, and how old it is.",
        "amplify": ['NONE',True]
    },
    "Diaboli : Void": {
        "rarity": 100400,
        "display": fg("Diaboli : Void", 55),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Undead : Devil": {
        "rarity": 120000,
        "display": (fg("Undead : Devil", 203)),
        "description": "silly tiny demon",
        "amplify": ['Hell',True]
    },
    "Comet": {
        "rarity": 120000,
        "display": (fg("COMET", 159)),
        "description": "People believe that it has the capabilities to make wishes come true.",
        "amplify": ['Starfall',True]
    },
    "Jade": {
        "rarity": 120000,
        "display": (fg("Jade", 29)),
        "description": "Where did it go?",
        "amplify": ['NONE',True]
    },
    "Spectre": {
        "rarity": 140000,
        "display": (fg("Spectre", 67)),
        "description": "Where did it go?",
        "amplify": ['NONE',True]
    },
    "Jazz": {
        "rarity": 160000,
        "display": (fg("Jazz", 215)),
        "description": "Jazz, a romance born in improvisation, where free melodies whisper the language of love.",
        "amplify": ['NONE',True]
    },
    "Aether": {
        "rarity": 180000,
        "display": (fg("Aether", 194)),
        "description": "Mysterious matter believed to act as a medium for transmitting light The exact use is unknown.",
        "amplify": ['NONE',True]
    },
    "Bounded": {
        "rarity": 200000,
        "display": fg("BOUNDED", 17),
        "description": "It's too dangerous. Although it was sealed by an Ancient Power hundreds of thousands of years ago, its consciousness appears to be alive",
        "amplify": ['NONE',True]
    },
    "Celestial": {
        "rarity": 350000,
        "display": fg("Celestial", 219),
        "description": "An Individual with a sacredness that seems to have descended from heaven is havering around and delivering words of blessing.",
        "amplify": ['NONE',True]
    },
    "Kyawthuite": {
        "rarity": 850000,
        "display": fg("Kyawthuite", 129),
        "description": "once in a thousand years, in the deepest part of the forest...",
        "amplify": ['NONE',True]
    },

    # 1,000,000 - Mythic
    "Arcane": {
        "rarity": 1000000,
        "display": fg("Arcane", 117),
        "description": "A spell found in the ruins of an ancient civilization.",
        "amplify": ['NONE',True]
    },
    "Magnetic : Reverse Polarity": {
        "rarity": 1024000,
        "display": fg("Magnetic : Reverse Polarity", 127),
        "description": "A collection of strong energies with inverted directions of acting polarities, which are not described magnetically.",
        "amplify": ['NONE',True]
    },
    "Undefined": {
        "rarity": 1111000,
        "display": fg("[Undefined]", 250),
        "description": "It's too dark in here...",
        "amplify": ['Null',True]
    },
    "Rage : Brawler": {
        "rarity": 1280000,
        "display": fg("Rage : Brawler", 196),
        "description": "flame of emotions",
        "amplify": ['NONE',True]
    },
    "Astral": {
        "rarity": 133600,
        "display": fg("Astral", 135),
        "description": "In the distant expanse of space, tiny stars emitting faint light come together to form a unified existence.",
        "amplify": ['Corruption',True]
    },
    "Cosmos": {
        "rarity": 1520000,
        "display": fg("Cosmos", 183),
        "description": "A galactic warrior who fought in the ancient space war. Countless years have passed since the war, but the scars of war still remains on its body.",
        "amplify": ['NONE',True]
    },
    "Gravitational": {
        "rarity": 2000000,
        "display": fg("Gravitational", 69),
        "description": "The irregularities of gravity incomprehensible to humans. It is thought to stem from the same material comprising the mysterious Great Attractor.",
        "amplify": ['NONE',True]
    },
    "Bounded : Unbound": {
        "rarity": 2000000,
        "display": fg("BOUNDED : UNBOUND", 21),
        "description": "When news spread that this being had awoken, people trembled in fear.",
        "amplify": ['NONE',True]
    },
    "Virtual": {
        "rarity": 2500000,
        "display": fg("Virtual", 87),
        "description": "An advanced hologram device created by an unnamed civilization.",
        "amplify": ['NONE',True]
    },
    "Savior": {
        "rarity": 3200000,
        "display": fg("Savior", 207),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Poseidon": {
        "rarity": 4000000,
        "display": fg("Poseidon", 44),
        "description": "It has been shaped as a creature that once ruled the ocean long ago.",
        "amplify": ['Rainy',True]
    },
    "Aquatic : Flame": {
        "rarity": 4000000,
        "display": fg("Aquatic : Flame", 208),
        "description": "It represents the flow of the flames",
        "amplify": ['NONE',True]
    },
    "Zeus": {
        "rarity": 4500000,
        "display": fg("Zeus", 229),
        "description": "It has the image of a creature that once ruled the sky.",
        "amplify": ['NONE',True]
    },
    "Galaxy": {
        "rarity": 5000000,
        "display": fg("Galaxy", 141),
        "description": "It comes from an unbelievably vast space itself.",
        "amplify": ['Starfall',True]
    },
    "Lunar : Full Moon": {
        "rarity": 5000000,
        "display": fg("Lunar : Full Moon", 229),
        "description": "A Full Moon hung in the sky",
        "amplify": ['NONE',True]
    },
    "Solar : Solstice": {
        "rarity": 5000000,
        "display": fg("Solar : Solstice", 228),
        "description": "It was made with Sunshine by an Unknown being on a bright day.",
        "amplify": ['NONE',True]
    },
    "Twilight": {
        "rarity": 6000000,
        "display": fg("Twilight", 147),
        "description": "A jewel that shines brightly once every thousand years in the deepest part of the forest.",
        "amplify": ['NONE',True]
    },
    "Origin": {
        "rarity": 6500000,
        "display": fg("Origin", 110),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Hades": {
        "rarity": 6666666,
        "display": fg("Hades" , 166),
        "description": "It has been shaped as the ruler of hell, a long time ago. Though not replicated perfectly, it still remains cruel and callous.",
        "amplify": ['Hell',True]
    },
    "Celestial : Divine": {
        "rarity": 7000000,
        "display": fg("CELESTIAL : DIVINE", 219),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Hypervolt": {
        "rarity": 7500000,
        "display": fg("HYPERVOLT", 177),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Velocity": {
        "rarity": 7630000,
        "display": fg("VELOCITY", 172),
        "description": "The power continuously accelerates objects until they burn up from friction.",
        "amplify": ['NONE',True]
    },
    "Anubis": {
        "rarity": 8500000,
        "display": fg("Anubis", 179),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Nihillity": {
        "rarity": 9000000,
        "display": fg("Nihillity", 248),
        "description": "Empty",
        "amplify": ['Null',True]
    },
    "Helios": {
        "rarity": 9000000,
        "display": fg("Helios", 221),
        "description": "In the mythology, A shining god of the sun. They rode their chariot to pull the Sun from the east to the west, making the cycle of day and night",
        "amplify": ['NONE',True]
    },

    # 10,000,000 - Exalted
    "Starscourge": {
        "rarity": 10000000,
        "display": fg("Starscourge", 210),
        "description": "When the stars aligned... the brightest starlights gathered to form this.",
        "amplify": ['Starfall',True]
    },
    "Sailor": {
        "rarity": 12000000,
        "display": fg("Sailor", 81),
        "description": "No one knows when this rusted fishing boat started its sail",
        "amplify": ['Rainy',True]
    },
    "Glitched": {
        "rarity": 12210110,
        "display": (fg("G", 232) + fg("L", 250) + fg("I", 234) + fg("T", 250) + fg("C", 252) + fg("H", 245)),
        "description": "WHAT ? NO, IT'S RIDICULOUS. IT SHOULDN'T HAPPEN",
        "amplify": ['Glitched',False]
    },
    "Stormal : Hurricane": {
        "rarity": 13500000,
        "display": (fg("Stormal : Hurricane", 249)),
        "description": "An enormous storm raging around you.",
        "amplify": ['Windy',True]
    },
    "Sirius": {
        "rarity": 14000000,
        "display": (fg("Sirius", 222)),
        "description": "A beautiful star that always faces you when I look at the night sky.",
        "amplify": ['Starfall',True]
    },
    "Arcane : Legacy": {
        "rarity": 15000000,
        "display": fg("Arcane : Legacy", 117),
        "description": "A spell found in the ruins of an ancient civilization. Maybe it was... too powerful.",
        "amplify": ['NONE',True]
    },
    "Blizzard": {
        "rarity": 19725000,
        "display": (fg("Blizzard", 117)),
        "description": "Empty",
        "amplify": ['Snowy',True]
    },
    "Chromatic": {
        "rarity": 20000000,
        "display": (fg("C", 196) + fg("H", 202) + fg("R", 226) + fg("O", 82) + fg("M", 48) + fg("A", 39) + fg("T", 99) + fg("I", 201) + fg("C", 196)),
        "description": "Yes... Feel my unstoppable beats!",
        "amplify": ['NONE',True]
    },
    "Aviator": {
        "rarity": 24000000,
        "display": (fg("★ AVIATOR ★", 185)),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Arcane : Dark": {
        "rarity": 30000000,
        "display": fg("Arcane : Dark", 93),
        "description": "A spell found in the ruins of an ancient civilization. This dreadful entity, no longer a mere spell, now is a sentient being",
        "amplify": ['NONE',True]
    },
    "Ethereal": {
        "rarity": 35000000,
        "display": (fg("Ethereal", 218)),
        "description": "In a country where the vast majority of people attend church, there is a deep-rooted belief in powers, either from God or from the 'dark side'.",
        "amplify": ['NONE',True]
    },
    "Overseer": {
        "rarity": 45000000,
        "display": (fg("Overseer", 153)),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Exotic : APEX": {
        "rarity": 49999500,
        "display": (fg("Exotic : APEX", 85)),
        "description": "Maybe this is the source of the ancient being, that people were dying to know about?",
        "amplify": ['NONE',True]
    },
    "Matrix": {
        "rarity": 50000000,
        "display": (fg("Matrix", 157)),
        "description": "No one can see, hear or touch this; perhaps, it might not even be real.",
        "amplify": ['NONE',True]
    },
    "Twilight : Iridescent Memory": {
        "rarity": 60000000,
        "display": fg("Twilight : Iridescent Memory", 225),
        "description": "The memories were becoming increasingly blurry. Under the full moon that holds many dreams high above, I sincerely wish.",
        "amplify": ['NONE',True]
    },
    "Sailor : Flying Dutchman": {
        "rarity": 80000000,
        "display": fg("Sailor : Flying Dutchman", 76),
        "description": "The Flying Dutchman. The same terrible vessel whose very timbers are cut from the bodies and souls of doomed seamen.",
        "amplify": ['Rainy',True]
    },


    # 99,999,999 - Glorious
    "Chromatic:Genesis": {
        "rarity": 99999999,
        "display": (fg("CHROMATIC : GENESIS", 153)),
        "description": "WAKE UP FROM AWAY",
        "amplify": ['NONE',True]
    },
    "Starscourge : Radiant": {
        "rarity": 100000000,
        "display": fg("Starscourge : Radiant", 117),
        "description": "When the stars aligned... the brightest starlights gathered to form this.",
        "amplify": ['Starfall',True]
    },
    "Overture": {
        "rarity": 150000000,
        "display": fg("Overture", 27),
        "description": "Inexorably, time flows forward cruelly. It cannot be stopped, or changed in direction. Perhaps time is a concept that exists in a dimension higher than the one we live in?",
        "amplify": ['NONE',True]
    },
    "Symphony": {
        "rarity": 175000000,
        "display": fg("Symphony", 153),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
    "Impeached": {
        "rarity": 200000000,
        "display": (fg("IMPEACHED", 206)),
        "description": "What's left for this fallen ruler?",
        "amplify": ['Corruption',True]
    },
    "Oppression": {
        "rarity": 220000000,
        "display": (fg("O", 255) + fg("p", 249) + fg("p", 238) + fg("r", 255) + fg("e", 238) + fg("s", 245) + fg("s", 250) + fg("i", 238) + fg("o", 243) + fg("n", 247)),
        "description": "... is this truly the end?",
        "amplify": ['Glitched',False]
    },
    "Archangel": {
        "rarity": 250000000,
        "display": (fg("Archangel", 229)),
        "description": "The most pure, beautiful, and holy being, in the mythology",
        "amplify": ['NONE',True]
    },
    "Exotic : VOID": {
        "rarity": 299999999,
        "display": (fg("Exotic : VOID", 165)),
        "description": "Nobody knows where it originates from, and how old it is.",
        "amplify": ['NONE',True]
    },
    "Overture : History": {
        "rarity": 300000000,
        "display": fg("OVERTURE : HISTORY", 48),
        "description": "When the clock hand started to move for the first time, was when everything started to move for the first time...",
        "amplify": ['NONE',True]
    },
    "Bloodlust": {
        "rarity": 300000000,
        "display": fg("BLOODLUST", 160),
        "description": "This doesn't represent anything inferior like a vampire or something, but rather never-ending thirst for blood itself.",
        "amplify": ['NONE',True]
    },
    "Jazz : Ochestra": {
        "rarity": 336870912,
        "display": fg("♩ Orchestra ♩", 230),
        "description": "Jazz, a romance born in improvisation, where free melodies whisper the language of love.",
        "amplify": ['NONE',True]
    },
    "Atlas": {
        "rarity": 360000000,
        "display": fg("ATLAS", 11),
        "description": "It is said that in their final moments, the last remaining Titan stood alone, upholding the celestial sphere.",
        "amplify": ['Sandstorm',True]
    },
    "Abyssal Hunter": {
        "rarity": 400000000,
        "display": (fg("ABYSSAL HUNTER", 27)),
        "description": "An unknown hunter, slaughtering deep sea creatures mercilessly and roaming around the trenches.",
        "amplify": ['NONE',True]
    },
    "Gargantua": {
        "rarity": 430000000,
        "display": (fg("GARGANTUA", 215)),
        "description": "It has existed since the beginning of the universe even now, it continues to devour everything that enters its domain, relentlessly moving forward.",
        "amplify": ['Starfall',True]
    },
    "Apostolos": {
        "rarity": 440000000,
        "display": (fg("APOSTOLOS", 167)),
        "description": "In mythological depictions, Apostolos represents the intersection of order and chaos. In his right hand rests the curse of chaos, and in his left hand, the blessing of order.",
        "amplify": ['NONE',True]
    },
    "Ruins": {
        "rarity": 500000000,
        "display": (fg("《 Ruins 》", 115)),
        "description": "In the ruins of an ancient civilization, destroyed by the destructive rituals and dark sorcery, only a place known as the Sanctuary remains, though it has crumbled in form.",
        "amplify": ['NONE',True]
    },
    "Matrix : Overdrive": {
        "rarity": 503000000,
        "display": (fg("{♢ MATRIX /◆ OVERDRIVE ♢}", 196)),
        "description": "C0re sys#ems ar# failing...... I. I. I. I. can't. can't. can't. ca. ..-. -. -.. th# ###ources... to fix myself.",
        "amplify": ['NONE',True]
    },
    "Matrix : Reality": {
        "rarity":  601020102,
        "display": (fg("MATRIX ▫ REALITY", 146)),
        "description": "They were all living in a simulation, This is the TRUE REALITY.",
        "amplify": ['NONE',True]
    },
    "Sovereign": {
        "rarity":  750000000,
        "display": (fg("SOVEREIGN", 153)),
        "description": "Look at this Shining Figure. Sovereign, revered as the most Glorious and Magnificent being among all rulers in history.",
        "amplify": ['NONE',True]
    },
    "Ruins : Withered": {
        "rarity": 800000000,
        "display": (fg("《 ⬥ Ruins : Withered ⬥ 》", 50)),
        "description": "Once radiant with sacred beauty, the ancient ruins of the spirits have become a nest for the dead and nightmares, twisted by a fallen lord.",
        "amplify": ['NONE',True]
    },
    "Aegis": {
        "rarity": 825000000,
        "display": (fg("(AEGIS)", 81)),
        "description": "Aegis, Named after the 'Shield of The Sky' Aegis is an anti-star satellite weapon currently being restored by the Science Foundation.",
        "amplify": ['NONE',True]
    },

    # 1,000,000,000 - Transcendents
    "Pixelation": {
        "rarity": 1073741824,
        "display": (fg('▣ ', 196) + fg('P', 202) + fg('I', 226) + fg('X', 82) + fg('L', 48) + fg('E', 39) + fg('A', 99) + fg('T', 201) + fg('I', 201) + fg('O', 201) + fg('N', 201) + fg(' ▣', 199)),
        "description": "“This description contains 0% lies and 1,000,000% TRUTH!”",
        "amplify": ['NONE',True]
    },
    "Luminosity": {
        "rarity": 1200000000,
        "display": (fg("[Luminosity]", 195) ),
        "description": "Empty",
        "amplify": ['NONE',True]
    },
}

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
        sys.stdout.write("\r" + fg(f"Rolling... {temp_aura['display']}               ", random.randint(232, 255)))
        sys.stdout.flush()
        time.sleep(speed)
        speed *= slowdown_rate

    # Final roll
    _, selected_aura = pick_aura(luck)
    display_name = selected_aura["display"]

    sys.stdout.write("\r" + fg(f"You rolled {display_name} !              ", random.randint(232, 255)))
    sys.stdout.flush()
    print("\n")

    # Update inventory using display
    if display_name in InventoryAuras:
        InventoryAuras[display_name] += 1
    else:
        InventoryAuras[display_name] = 1

    inventory(InventoryAuras)


def craft(recipe: dict):
    requirement = 0
    completion = 0
    Incomplete = {}
    for item in recipe:
        if item != "Display":
            requirement += 1
            if item in InventoryAuras:
                if InventoryAuras[item] >= recipe[item]:
                    completion += 1
                    print(recipe[item])
                else:
                    print("no")
                    if item in Incomplete:
                        Incomplete[item] += 1
                    else:
                        Incomplete[item] = 1
        else:
            display = recipe["Display"]

    if requirement == completion:
        print("you crafted cool thing woo")
        for item in recipe:
            if item != "Display":
                InventoryAuras[item] -= recipe[item]
        if display in InventoryAuras:
            InventoryAuras[display] += 1
        else:
            InventoryAuras[display] = 1
    else:
        print("you did not craft thing boo")
        print(Incomplete)


    inventory(InventoryAuras)


InventoryAuras = {}

def inventory(inventory : dict) -> None:
    print(LINE)
    print(fg("Inventory", 220))
    print(LINE)
    for name, count in inventory.items():
        print(f"{name} : {count}")

Recipe = {
    "Gear Basing": {Auras["Common"]["display"] : 1, Auras["Uncommon"]["display"] : 1, Auras["Good"]["display"] : 1, Auras["Rare"]["display"] : 1, "Display" : fg("Gear Basing",245)}
}

# LUCK = ((1 + Basic Luck) * Bonus Roll + Special Buff) * VIP
luck = 10
rollspeed = math.inf

for i in range(1000):
    Roll(luck,rollspeed)


craft(Recipe["Gear Basing"])