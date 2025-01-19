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

