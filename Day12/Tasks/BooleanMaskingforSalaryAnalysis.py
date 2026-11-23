import numpy as np

salaries = np.array([25000, 40000, 15000, 50000, 30000])

# Filter salaries above 30000
filtered = salaries[salaries > 30000]

print("Salaries Above 30000:", filtered)

# Count employees
count = np.sum(salaries > 30000)

print("Number of Employees:", count)