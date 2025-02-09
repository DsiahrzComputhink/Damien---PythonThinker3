class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    RESET = '\033[0m'

test1 = "ONE"
test2 = "TWO"

print(style.RED + "RED TEXT" + style.RESET)
print(style.GREEN + "GREEN TEXT" + style.RESET)