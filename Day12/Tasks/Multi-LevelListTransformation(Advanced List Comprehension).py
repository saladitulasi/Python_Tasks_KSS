data = [[1, 2, 3], [4, 5], [6]]

# Flatten the nested list
flat_list = [num for sublist in data for num in sublist]

print("Flattened List:", flat_list)

# Square only even numbers
squares = [num**2 for num in flat_list if num % 2 == 0]

print("Squares of Even Numbers:", squares)