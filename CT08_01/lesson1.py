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
print(fruitcost[0]) # 100

print(f"The price of an orange is{fruitcost["Orange"]}")

fruitcost["Watermelon"] = 10.35
print(fruitcost)