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

# silly challenge: make a fast food restruant

menu = {
    "Notebook":5.50,
    "Pencil":5.30,
    "Backpack":3.00,
    "whatever this is":4.80,
    "Pen":2.20,
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
    print("{:^10}Welcome to the Bookshop!{:^10}".format('*'*10, '*'*10,))
    print("--------------Menu---------------")
    
    # Format
    for food, price in menu.items():
        print("{:20}:     ${:^8.2f}".format(food, price))

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