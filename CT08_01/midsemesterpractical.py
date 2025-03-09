my_list = [5, 8, 10, 9, 11, 12, 15, 2]
n = len(my_list)

# For i in range,
for i in range(n+1):
    # For each number in the list,
    for j in range(0, n-1):
        # If 
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print(my_list)