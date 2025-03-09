# Bubble sort algorithm
my_list = [96, 94, 99, 78, 14, 63, 73, 70, 38, 3, 53, 20, 27, 32, 89]
n = len(my_list)

# For i in range,
for i in range(n+1):
    # For each number in the list,
    for j in range(0, n-1):
        # If current number is smaller than the number next to it,
        if my_list[j] < my_list[j+1]:
            # Swap positions with both numbers
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

# Print out list
print(my_list)