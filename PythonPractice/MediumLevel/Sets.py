list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

set1 = set(list1)
set2 = set(list2)

# Common elements
common = set1 & set2

# Elements only in the first list
only_first = set1 - set2

# All unique elements
all_unique = set1 | set2

print("Common elements:", common)
print("Only in first list:", only_first)
print("All unique elements:", all_unique)