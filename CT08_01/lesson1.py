# DICTIONARY
fruit = ["Apple","Orange","Banana"]
costs = [1.50 , 2.55, 4.25]
# Can be
fruitcost = {"Apple": 1.50, "Orange": 2.55, "Banana": 4.25}
# Key Value is to the left
# The right side is the value

var = "var"
print("This is a",var,"iable")
print(f"this is a {var}iable")

# Acessing a dictionary value
print(fruitcost)

print(f"The price of an orange is {fruitcost["Orange"]}")

# Appending a new item to a dictionary
fruitcost["Durian"] = 24.40
print(fruitcost)

# Deleting a item from the list
del fruitcost["Apple"]
print(f"Fruit Store:{fruitcost}")

# Iterating through a dictionary
for fruit in fruitcost:
    price = fruitcost[fruit]
    print(f"{fruit} costs {price}")

# Method 2
print(fruitcost.keys())
print(fruitcost.values())
print(fruitcost.items())

# silly challenge: make a fast food restruant

menu = {
    "Cheeseburger":5.50,
    "Hamburger":5.30,
    "Fries":3.00,
    "Cheese fries":4.80,
    "Milo":2.20,
    }

ordered = {}

def display_menu(menu, ordered):
    # Display Menu

    print("---------------------------------")
    print("{:^10}Welcome to Resturant{:^10}".format('*'*10, '*'*10,))
    print("--------------Menu---------------")
    
    # Format
    for food, price in menu.items():
        print("{:20}:     ${:^8.2f}".format(food, price))

    print("---------------------------------")

    stop = 0
    itemordered = 0
    # variables

    while stop == 0:
    # ask what to order
        if itemordered == 0:

            print("What would you like to order?")
            order = input("")

        else:

            print("Anything else you like to order?")
            order = input("")
            
        #Self correction
        order = order.capitalize()
        print(order)

        if order in menu:
            print(f"{order} has been added to your order")
            ordered[order] = menu[order]
        else:
            print(f"Sorry, we dont sell {order}")
        itemordered == 1




display_menu(menu, ordered)