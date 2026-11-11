

from utilities import math_operations
from utilities import string_operations

# Mathematical operations
num1 = 10
num2 = 5

print("Addition:", math_operations.addition(num1, num2))

print("Multiplication:",
      math_operations.multiplication(num1, num2))

# String operations
text = input("Enter a string: ")

print("Uppercase:", string_operations.to_uppercase(text))

print("Character count:",
      string_operations.count_characters(text))
