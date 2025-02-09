class style():
  RED = '\033[31m'
  GREEN = '\033[32m'
  BLUE = '\033[34m'
  RESET = '\033[0m'

test1 = "ONE"
test2 = "TWO"

print(style.RED + "{0}".format(test1) + style.RESET)
print(style.GREEN + "TESTING" + style.RESET)