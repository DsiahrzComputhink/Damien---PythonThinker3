import random

numbers = []

for i in range(10):
    x = random.randint(1,10000)
    numbers.append(x)

print(numbers)

def bubblesort(numbers):
    for i in range(100):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp
        return numbers
    print("Final Result")
    return numbers


print(bubblesort(numbers))