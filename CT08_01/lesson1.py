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


# --- The thing above is just for decorative stuff, it is not to concern with the code - Dsiahrz

# silly challenge the second: popular the store

menu = {
    "Notebook":2.00,
    "Pencil":0.50,
    "Backpack":17.50,
    "Eraser":0.60,
    "Ruler":2.00,
    }

ordered = {
    # -- Just Quantity
    "Notebook":0,
    "Pencil":0,
    "Backpack":0,
    "Eraser":0,
    "Ruler":0,
}

yes = {
    "yes",
    "ye",
    "yass",
    "positive",
    "thats all",
    "put the fries in the bag lil bro",
}

no = {
    "nuh uh",
    "yes'nt",
    "no",
    "nah",
    "not",
    "negative",
    "not yet",
    "thats all",
}


def display_menu(menu, ordered):
    # Display Menu
    LINE = style.bBLACK + "--------------------------------------------" + style.RESET


    print(LINE)
    print(style.bBLACK + "{:^10}Welcome to the Bookshop!{:^10}".format('*'*10, '*'*10,) + style.RESET)
    print(style.bBLACK + "--------------------Menu--------------------" + style.RESET)
    
    # Format
    for food, price in menu.items():
        print(style.bBLUE + "{:30}:     ${:^8.2f}".format(food, price) + style.RESET)

    print(LINE)
    print("For any purchase",style.bGREEN + "more than" + style.RESET, style.bCYAN + "$20.00" + style.RESET,",")
    print("You will get a", style.bYELLOW + "10%" + style.RESET ,"Discount!")

    print(LINE)
    print("Type in", style.bRED + "'Thats all'" + style.RESET ,"to stop ordering.")

    stop = 0
    itemordered = 0
    total = 0
    # variables

    # WHILE LOOP
    while stop == 0:
    # ask what to order
        if itemordered == 0:
            print("'What would you like to order?'")
            order = input("")

        else:
            print("'Anything else you like to order?'")
            order = input("")

        #Self correction
        order = order.capitalize()

        # if order
        if order == "Thats all":
            if ordered == {}:
                # anger
                print(style.dRED + "'Ok bro.'" + style.RESET)
                stop = 1
            else:
                print(style.bCYAN + "-------------Order---------------" + style.RESET)
                for food, price in ordered.items():
                    print(style.bCYAN + "{:20}Qnty:    {:^8.0f}".format(food, price) + style.RESET)
                print(style.bCYAN + "---------------------------------" + style.RESET)
                print("'Would that be all?'")
                answer = input("")
                answer = answer.lower()
                if answer in yes:
                    print("'Ok, your total will be'")
                    for food, price in ordered.items():
                        print(total)
                        total += price

                    print(style.bYELLOW + "${:^8.2f}".format(total) + style.RESET)
                    if total > 20:
                        print("Oh wait, your total is more than",style.bCYAN + "$20.00" + style.RESET,"!")
                        print("So your total will be")
                        total *= 0.9
                        print(style.bYELLOW + "${:^8.2f}".format(total) + style.RESET)
                        stop = 1
                    else:
                        stop = 1
                        break


                elif answer in no:
                    print("Ok,")


        elif order in menu:
            print("How much would you want to order?")
            amt = input("")
            print()
            if amt.isnumeric():
                if amt >= 5:
                    print("Are you sure?")
                    answer = input(style.bRED + "" + style.RESET)
                    if answer in yes:
                        print(style.bBLUE + f"{amt} {order}'s" + style.RESET," has been added to your order")
                        ordered[order] += int(amt)
                    else:
                        print("Ok")
                else:
                    print("Alright, the price of",style.bBLUE + f"{amt}{order}" + style.RESET,"is",)
            else:
                print("Sorry, thats not a defined quantity.")
        else:
            print(f"Sorry, we dont sell",style.bRED + {order} + style.RESET)
        itemordered = 1

display_menu(menu, ordered)