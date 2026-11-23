import numpy as np

sales = [10, 20, 30, 40, 50, 60,
         70, 80, 90, 100, 110, 120]

arr = np.array(sales)

new_arr = arr.reshape(4, 3)

print(new_arr)