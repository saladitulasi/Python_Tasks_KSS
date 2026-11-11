def list_sum(numbers):
    total = 0

    for n in numbers:
        total += n

    return total

numbers = [10, 20, 30, 40, 50]

print("Sum of list elements:", list_sum(numbers))