import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]]

# Create deep copy
copied_classes = copy.deepcopy(classes)

# Modify original data
classes[0][1][0] = 40

print("Original Data:", classes)
print("Copied Data:", copied_classes)