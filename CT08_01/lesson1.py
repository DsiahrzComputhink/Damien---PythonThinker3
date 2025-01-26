
menu = {
    "Cheeseburger":"$5.50",
    "Fries":"$3.00",
    "Milo":"$2.20",
    }

def display_menu(menu):
    print("---------------------------------")
    print("{:^10}Welcome to Resturant{:^10}".format('*'*10, '*'*10,))
    print("--------------Menu---------------")
    for food, price in menu.items():
        print("{:^30}:${:^8.2f}".format(food, price))
    print("---------------------------------")
    #-- ask what to order
    print("What would you like to order?")
    input("")
    


    

display_menu(menu)