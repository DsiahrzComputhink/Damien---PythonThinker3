# am bored
import time

# LESSON 1
import random
numbers = [5, 4, 3, 2, 1]

def isascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            return False
    return True

isascending(numbers)


import random

# LESSON 2
# ALGORITHMS
numbers = []

for i in range(30):
    x = random.randint(1,100)
    numbers.append(x)

print("Unsorted List")
print(numbers)

def bubblesort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                time.sleep(0.01)
                print(numbers)
    return numbers

print("Sorted List")
print(bubblesort(numbers))