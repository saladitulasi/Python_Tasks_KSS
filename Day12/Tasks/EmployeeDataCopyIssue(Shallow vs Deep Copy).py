import copy

employees = [[101, "A"], [102, "B"], [103, "C"]]

# Shallow copy
shallow = copy.copy(employees)

employees[0][1] = "Z"

print("Original:", employees)
print("Shallow Copy:", shallow)

# Deep copy
deep = copy.deepcopy(employees)

employees[0][1] = "X"

print("Original after modification:", employees)
print("Deep Copy:", deep)