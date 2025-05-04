# Question 1
# You are given a dictionary representing a restaurant menu.
# Each key is a food item (string), and 
# each value is the price of the item (float).

# Your tasks are:
# 1. Loop through the dictionary to print out the food items they sell.
# 2. Ask the customer what they want to buy.
# 3. Check if the item exists in the menu. 
#    - If it exists, print: " costs $"
#    - If it does not exist, print: "Sorry, we don't sell that."

# Example Output:
# Menu:
# Pizza
# Burger
# Pasta
# ...
# What would you like to buy? Pasta
# Pasta costs $6.9
###########################################
# Task: Complete the code below

menu = {
    "Pizza": 8.5,
    "Burger": 5.0,
    "Pasta": 6.9,
    "Fries": 3.5,
    "Salad": 4.0,
    "Sushi": 10.5,
    "Steak": 12.0,
    "Taco": 4.2,
    "Curry": 7.3,
    "Soup": 3.9
}


# Part 1: LOOP THROUGH THE MENU AND PRINT ITEMS
# Part 2: ASK THE USER WHAT THEY WANT TO BUY
# Part 3: CHECK IF ITEM EXISTS AND PRINT THE PRICE

# Write your code here, add more space as required
LINE = "------------------------------------"

print(LINE)
print("Welcome to the Restruant!")
print(LINE)
print("MENU:")
for key in menu: # Iterate through the menu
    print(f"{key} : ${menu[key]:.2f}")
print(LINE)
while True:
    print("What would you like to order?")
    order = input("")
    if order.capitalize() in menu:
        print(f"That item costs ${menu[order.capitalize()]:.2f}")

##########################################################