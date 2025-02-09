class style():
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
    "Backpack":20.00,
    "Eraser":0.60,
    "Ruler":2.00,
    }

ordered = {}

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

    print("---------------------------------")
    print("{:^10}Welcome to the Bookshop!{:^10}".format('*'*8, '*'*8,))
    print("--------------Menu---------------")
    
    # Format
    for food, price in menu.items():
        print(style.bBLUE + "{:20}:     ${:^8.2f}".format(food, price) + style.RESET)

    print("---------------------------------")
    print("Type in 'Thats all' to stop ordering.")

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
                print("'ok bro.'")
                stop = 1
            else:
                print("-------------Order---------------")

                for food, price in ordered.items():
                    print("{:20}:     ${:^8.2f}".format(food, price))

                print("---------------------------------")
                print("'Would that be all?'")
                answer = input("")
                answer = answer.lower()
                if answer in yes:
                    print("'Ok, your total will be'")
                    for food, price in ordered.items():
                        print(total)
                        total += price
                    print("{:^8.2f}".format(total))

                elif answer in no:
                    print("Ok,")


        elif order in menu:
            print(f"{order} has been added to your order")
            ordered[order] = menu[order]
        else:
            print(f"Sorry, we dont sell {order}")
        itemordered = 1



display_menu(menu, ordered)