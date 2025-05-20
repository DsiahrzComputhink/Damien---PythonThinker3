import random
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

def status(num: int, name: str, variable: int):
    print(style.bblue + f"[{num}]" + style.RESET, f"{name}:" , variable,"/ 100")

class Tamagotchi:
    def __init__(self,name : str):
        self.name = name
        self.hunger = 50 # Hunger level (0 = full, 100 = starving)
        self.energy = 50 # Energy level ( 0 = exhausted, 100 = full of energy)
        self.happiness = 50 # Happiness level (0 = sad, 100 = very happy)
        self.age = 0 # Age in virtual days

    def attributes(self): # DEBUG
        print(f"Name: {self.name} | Hunger: {self.hunger} | Energy: {self.energy} | Happiness: {self.happiness} | Age: {self.age}")
    
    def status(self):

        print(LINE)
        print(style.BOLD + f"{self.name}'s Status" + style.RESET)
        print(LINE)
        status(1,"Hunger",self.hunger)
        status(2,"Energy",self.energy)
        status(3,"Happiness",self.happiness)
        print(style.bblue + f"[4]" + style.RESET, f"Age:" , self.age,"days ")
    
    def feed(self):
        randomnum = random.randint(5,15)
        randomnum2 = random.randint(1,5)
        randomnum3 = random.randint(5,10)
        self.hunger = max(self.hunger - randomnum, 0)
        self.energy = min(self.energy + randomnum2, 100)
        self.happiness = min(self.happiness - randomnum3, 100)
        print(LINE)
        print("You fed",style.BOLD + f"{name}" + style.RESET,"!")
        print(style.bcyan + "Hunger" + style.RESET,"went down by",style.bgreen + f"{randomnum}" + style.RESET)
        print(style.bcyan + "Energy" + style.RESET,"went up by",style.bgreen + f"{randomnum2}" + style.RESET)
        print(style.bcyan + "Happiness" + style.RESET,"went down by",style.bred + f"{randomnum3}" + style.RESET)

    def play(self):
        randomnum = random.randint(5,10)
        randomnum2 = random.randint(15,20)
        randomnum3 = random.randint(10,15)
        self.hunger = min(self.hunger + randomnum, 0)
        self.energy = min(self.energy - randomnum2, 0)
        self.happiness = min(self.happiness + randomnum3, 100)
        print(LINE)
        print(style.BOLD + f"{name}" + style.RESET,"went to sleep!")
        print(style.bcyan + "Hunger" + style.RESET,"went up by",style.bred + f"{randomnum}" + style.RESET)
        print(style.bcyan + "Energy" + style.RESET,"went down by",style.bred + f"{randomnum2}" + style.RESET)
        print(style.bcyan + "Happiness" + style.RESET,"went up by",style.bgreen + f"{randomnum3}" + style.RESET)

    def sleep(self):
        randomnum = random.randint(10,15)
        randomnum2 = random.randint(15,20)
        randomnum3 = random.randint(5,10)
        self.hunger = max(self.hunger + randomnum, 100)
        self.energy = max(self.hunger + randomnum2, 100)
        self.happiness = max(self.hunger + randomnum3, 100)
        print(LINE)
        print(style.BOLD + f"{name}" + style.RESET,"went to sleep!")
        print(style.bcyan + "Hunger" + style.RESET,"went down by",style.bred + f"{randomnum}" + style.RESET)
        print(style.bcyan + "Energy" + style.RESET,"went up by",style.bgreen + f"{randomnum2}" + style.RESET)
        print(style.bcyan + "Happiness" + style.RESET,"went up by",style.bgreen + f"{randomnum3}" + style.RESET)

    def growolder(self):
        if self.hunger >= 100:
            print("Your pet died due to",style.bred + "[Starvation]" + style.RESET)
        elif self.energy <= 0:
            print("Your pet died due to",style.bred + "[Exhaustion]" + style.RESET)
        elif self.happiness <= 0:
            print("Your pet died due to",style.bred + "[Depression]" + style.RESET)
        else:
            if self.age < 15:
                self.age += 1
                print(style.BOLD + f"{name}" + style.RESET,"grew older!")
                print("Age:",style.bgreen + f"{self.age}" + style.RESET,"Days old")
            else:
                print(f"You sucessfully raised up {name}!")



name = input("Name your pet: ")
pet = Tamagotchi(str(name))

dead = 0
while dead == 0:
    pet.status()
    print(LINE)
    print(style.bblue + f"[1]" + style.RESET, f"Feed")
    print(style.bblue + f"[2]" + style.RESET, f"Play")
    print(style.bblue + f"[3]" + style.RESET, f"Sleep")
    print(style.bblue + f"[4]" + style.RESET, f"Quit")
    command = input()
    if command.isnumeric():
        if command == "1":
            pet.feed()
        elif command == "2":
            pet.play()
        elif command == "3":
            pet.sleep()
        elif command == "4":
            print("Program Closing...")
            dead = 1
        pet.growolder()