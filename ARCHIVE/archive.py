import random
numbers = [5, 4, 3, 2, 1]

def isascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            return False
    return True

isascending(numbers)