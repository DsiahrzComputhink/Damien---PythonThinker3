#  Debug the above sample code and print out the sorted list of numbers from largest to smallest.
#  Bubble sort algorithm
my_list = [87, 71, 85, 55, 77, 68, 76, 86, 56, 41, 43, 14, 5, 90, 37, 32, 60, 81, 34, 28, 29]
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


# 2nd Task
