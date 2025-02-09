class style():
  RED = '\033[31m'
  GREEN = '\033[32m'
  BLUE = '\033[34m'
  RESET = '\033[0m'

test1 = "ONE"
test2 = "TWO"

print(style.RED + "" + style.RESET)
print(style.GREEN + "GREEN TEXT" + style.RESET)