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

# -- RANGES
    # Uppercase Leters: 65 - 90
    # Lowercase Letters: 97 - 122
    # Digits: 48 - 57
    # Symbols: 33 - 47, 58 - 64, 91 - 96


# ASCII User Management System (UMS)

# Must DO:
# * Create new users with automatically generated strong passwords.
# * Update existing passwords by verifiying the current one.
# * View usernames and their masked passwords.
# * Access all features through a interactive menu system.