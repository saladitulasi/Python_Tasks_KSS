import numpy as np
import pandas as pd
import math

# Generate random student marks
marks = np.random.randint(30, 101, 10)

# Create student names
names = ["Arun", "Bala", "Charan", "Divya", "Esha",
         "Farhan", "Gita", "Hari", "Isha", "John"]

# Convert into Pandas DataFrame
data = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print("Student Data:")
print(data)

# Filter passing students
passing = data[data["Marks"] >= 40]

print("\nPassing Students:")
print(passing)

# Calculate average using NumPy
average = np.mean(marks)

print("\nAverage Marks:", math.ceil(average))

# Print results using loop
print("\nStudent Results:")

for index, row in data.iterrows():
    if row["Marks"] >= 40:
        print(row["Name"], "- Pass")
    else:
        print(row["Name"], "- Fail")