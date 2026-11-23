import numpy as np

arr = np.array([10, 20, 30, 40])

view_arr = arr.view()

arr[0] = 100

print("Original Array:", arr)
print("View Array:", view_arr)