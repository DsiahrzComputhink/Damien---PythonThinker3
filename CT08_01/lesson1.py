class style():
    # d = DARK
    # b = BRIGHT

    #bg-d = BACKGROUND DARK
    #bg-b = BACKGROUND BRIGHT
    dBLACK = '\033[30m'
    dRED = '\033[31m'
    dGREEN = '\033[32m'
    dYELLOW = '\033[33m'
    dBLUE = '\033[34m'
    dPURPLE = '\033[35m'
    dCYAN = '\033[36m'
    dWHITE = '\033[37m'

    bBLACK = '\033[90m'
    bRED = '\033[91m'
    bGREEN = '\033[92m'
    bYELLOW = '\033[93m'
    bBLUE = '\033[94m'
    bPURPLE = '\033[95m'
    bCYAN = '\033[96m'
    bWHITE = '\033[97m'

    RESET = '\033[0m'

test1 = "ONE"
test2 = "TWO"

print(style.bCYAN + "RED TEXT" + style.RESET)
print(style.bGREEN + "GREEN TEXT" + style.RESET)