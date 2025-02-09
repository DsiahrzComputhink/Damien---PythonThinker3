class style():

    d_black = '\033[30m'
    d_red = '\033[31m'
    d_green = '\033[32m'
    d_yellow = '\033[33m'
    d_blue = '\033[34m'
    d_purple = '\033[35m'
    d_cyan = '\033[36m'
    d_white = '\033[37m'

    b_black = '\033[30m'
    b_red = '\033[31m'
    b_green = '\033[32m'
    b_yellow = '\033[33m'
    b_blue = '\033[34m'
    b = '\033[35m'
    break_cyan = '\033[36m'
    b_white = '\033[37m'

    RESET = '\033[0m'

test1 = "ONE"
test2 = "TWO"

print(style.bCYAN + "RED TEXT" + style.RESET)
print(style.bGREEN + "GREEN TEXT" + style.RESET)