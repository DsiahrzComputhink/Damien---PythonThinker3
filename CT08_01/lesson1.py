class style():
    # d = DARK
    # b = BRIGHT
    dBLACK = '\033[40m'
    dRED = '\033[41m'
    dGREEN = '\033[42m'
    dYELLOW = '\033[43m'
    dBLUE = '\033[44m'
    dPURPLE = '\033[45m'
    dCYAN = '\033[46m'
    dWHITE = '\033347m'

    bBLACK = '\033[100m'
    bRED = '\033[101m'
    bGREEN = '\033[102m'
    bYELLOW = '\033[103m'
    bBLUE = '\033[104m'
    bPURPLE = '\033[105m'
    bCYAN = '\033[106m'
    bWHITE = '\033[107m'

    # BACKGROUNDS
    #bgd = BACKGROUND DARK
    #bgb = BACKGROUND BRIGHT
    d_black = '\033[30m'
    d_red = '\033[31m'
    d_green = '\033[32m'
    d_yellow = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    dwhite = '\033[37m'

    bgbBLACK = '\033[90m'
    bgbRED = '\033[91m'
    bgbGREEN = '\033[92m'
    bgbYELLOW = '\033[93m'
    bgbBLUE = '\033[94m'
    bgbPURPLE = '\033[95m'
    bgbCYAN = '\033[96m'
    bgbWHITE = '\033[97m'

    RESET = '\033[0m'

test1 = "ONE"
test2 = "TWO"

print(style.bCYAN + "RED TEXT" + style.RESET)
print(style.bGREEN + "GREEN TEXT" + style.RESET)