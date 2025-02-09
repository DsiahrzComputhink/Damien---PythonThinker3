import random

class style:
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

# Define characters
words = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_'
]

# Generate a random password length
PASSWORDLENGTH = random.randint(8, 20)  # Change the range as needed
print(f"Password Length: {PASSWORDLENGTH}")

# Generate the password
password_chars = [random.choice(words) for _ in range(PASSWORDLENGTH)]
password_string = " ".join(password_chars)  # Join with spaces

# Print the password
print(style.bcyan + "Password:" + style.RESET, style.bwhite + password_string + style.RESET)


stop = 0

# The Game
while stop == 0:
    LINE = "--------------------------------------------"
    print(style.bgray + LINE + style.RESET)
    print(style.bred + "{:^10}Type in command to start{:^10}".format(' '*10, ' '*10,) + style.RESET)
    print(style.bgray + "--------------------Cmds--------------------" + style.RESET)
    print(style.bblue + "{:^10} corrupt . {:^10}".format(' '*10, ' '*10,) + style.RESET)

    print(LINE)
    print("For any purchase",style.bGREEN + "more than" + style.RESET, style.bCYAN + "$20.00" + style.RESET,",")
    print("You will get a", style.bYELLOW + "10%" + style.RESET ,"Discount!")

    print(LINE)
    print("Type in", style.bRED + "'Thats all'" + style.RESET ,"to stop ordering.")

    cmd = input("")