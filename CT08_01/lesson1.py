import random

numbers = []

for i in range(10):
    x = random.randint(1,10000)
    numbers.append(x)

print("Unsorted List")
print(numbers)

def bubblesort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

print("Sorted List")
print(bubblesort(numbers))
