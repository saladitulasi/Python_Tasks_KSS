import numpy as np

arr = [-5, 10, 15, -2, 20, 25, 30]

# Convert list into NumPy array
np_arr = np.array(arr)

# Filter positive even numbers
result = np_arr[(np_arr > 0) & (np_arr % 2 == 0)]

print("Original Array:", np_arr)
print("Positive Even Numbers:", result)