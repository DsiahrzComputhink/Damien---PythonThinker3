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

def colorstatus(num: int):
    if num >= 0:
        return style.bblue + {num} + style.RESET, "/ 100"

class Tamagotchi:
    def __init__(self,name : str):
        self.name = name
        self.hunger = 50 # Hunger level (0 = full, 100 = starving)
        self.energy = 50 # Energy level ( 0 = exhausted, 100 = full of energy)
        self.happiness = 50 # Happiness level (0 = sad, 100 = very happy)
        self.age = 50 # Age in virtual days

    def attributes(self): # DEBUG
        print(f"Name: {self.name} | Hunger: {self.hunger} | Energy: {self.energy} | Happiness: {self.happiness} | Age: {self.age}")
    
    def status(self):
        print(style.BOLD + f"{self.name}'s Status" + style.RESET)
        print(style.bblue + "[1]" + style.RESET, "Hunger:" , colorstatus(self.hunger))

name = "Roger"
pet = Tamagotchi(name)
pet.status()