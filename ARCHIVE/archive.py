# TO TEST OUT

#------------------
# LESSON 2
# ALGORITHMS
numbers = []

for i in range(1000):
    x = random.randint(1,1000)
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
