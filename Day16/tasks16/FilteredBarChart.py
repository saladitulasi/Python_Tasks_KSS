import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

# Create DataFrame
df = pd.DataFrame({
    "Names": names,
    "Marks": marks
})

print("Original Data:")
print(df)

# Filter students with marks > 50
filtered = df[df["Marks"] > 50]

print("Filtered Data:")
print(filtered)

# Plot bar chart
plt.bar(filtered["Names"], filtered["Marks"],
        color='green')

# Add labels and title
plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.title("Students Scoring Above 50")

plt.show()