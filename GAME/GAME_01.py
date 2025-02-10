def bruteforcegame():
    import random
    import time

    class style:
        BOLD = '\033[1m'
        ITALIC = '\033[3m'
        UNDERLINE = '\033[4m'
        CANCEL = '\033[9m'

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
    PASSWORDLENGTH = random.randint(8, 50)  # Change the range as needed
    print(f"Password Length: {PASSWORDLENGTH}")

    # Generate the password
    password_chars = [random.choice(words) for _ in range(PASSWORDLENGTH)]
    password_string = " ".join(password_chars)  # Join with spaces

    # Print the password
    print(style.bcyan + "Password:" + style.RESET, style.bwhite + password_string + style.RESET)


    menu_text = f"""
    {style.bgray}--------------------------------------------{style.RESET}
    {style.bred}{' ' * 10}Type in command to start{' ' * 10}{style.RESET}
    {style.bgray}--------------------Cmds--------------------{style.RESET}

    {style.bblue}bruteforce.password{style.RESET} . {style.bblue}[CRACK PASSWORD]{style.RESET}          
    {style.bblue}menu{style.RESET} . {style.bblue}[SHOW MENU]{style.RESET}          

    {style.bgray}--------------------------------------------{style.RESET}
    """

    stop = False
    # The Game

    print(menu_text)
    while not stop:

        print("Waiting for command input...")

        cmd = input("").strip().lower()

        if cmd == "bruteforce.password":
            print(style.bred + "Starting brute force attack..." + style.RESET)

            TIME = 0.2
            guessed_password = ""
            for target_index, target_char in enumerate(password_string):
                for attempt in words:
                    print(style.dcyan + f"Trying: {guessed_password + attempt}..." + style.RESET, end="\r")

                    time.sleep(TIME)  # Simulate brute force delay
                    if TIME > 0.01:
                        TIME *= 0.99
                    elif TIME <= 0.01:
                        TIME *= 0.999
                    elif TIME <+ 0.0001:
                        TIME *= 0.999

                    
                    if attempt == target_char:
                        guessed_password += attempt
                        break  # Move to the next letter

            print("\n" + style.bgreen + f"Password Cracked! → {guessed_password}" + style.RESET)
        
        elif cmd == "menu":
            print(menu_text)
        else:
            print(style.dred + "Command not found." + style.RESET)