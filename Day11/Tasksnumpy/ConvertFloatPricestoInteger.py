import numpy as np

prices = [10.5, 20.8, 15.3]

arr = np.array(prices)

int_arr = arr.astype(int)

print("Original Array:", arr)
print("Integer Array:", int_arr)