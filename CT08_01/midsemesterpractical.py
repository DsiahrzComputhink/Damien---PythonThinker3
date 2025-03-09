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
# Dictionary
Scrabble = {
    "A": 1, 
    "B": 3, 
    "C": 3,
    "D": 2, 
    "E": 1, 
    "F": 4,
    "G": 2, 
    "H": 4, 
    "I": 1,
    "J": 8, 
    "K": 5, 
    "L": 1,
    "M": 3, 
    "N": 1, 
    "O": 1,
    "P": 3, 
    "Q": 10, 
    "R": 4,
    "S": 1, 
    "T": 1, 
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10,
}

# Asks for a input
print("Give me 5 words.")
input = input("")

# Capitalize to prevent any errors
word = input.upper()
print(word)
# For every character in word, find the value for the key
for i in word:
    print(Scrabble[i])