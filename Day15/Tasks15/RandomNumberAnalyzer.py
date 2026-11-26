import random

# Generate 10 random numbers
numbers = []

for i in range(10):
    num = random.randint(1, 100)
    numbers.append(num)

print("Random Numbers:", numbers)

# Count even and odd numbers
even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Numbers:", even)
print("Odd Numbers:", odd)

# Remove duplicates using set
unique_numbers = set(numbers)

print("Unique Numbers:", unique_numbers)