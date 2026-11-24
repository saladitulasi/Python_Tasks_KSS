import numpy as np

nums = np.random.randint(1, 100, 10)
import numpy as np

# Generate 10 random numbers
nums = np.random.randint(1, 100, 10)

# Filter numbers divisible by 5
filtered_nums = nums[nums % 5 == 0]

# Sort the filtered numbers
sorted_nums = np.sort(filtered_nums)

print("Random Numbers:", nums)
print("Sorted Numbers Divisible by 5:", sorted_nums)