import random

numbers = []

for i in range(10):
    x = random.randint(1,10000)
    numbers.append(x)


def bubblesort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp
        return numbers

print("Unsorted List")
print(bubblesort(numbers))
