import numpy as np

temperatures = [28, 31, 35, 27, 40, 22]

arr = np.array(temperatures)

result = arr[arr > 30]

print("Temperatures above 30°C:", result)