import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

# Create DataFrame
df = pd.DataFrame({
    "Names": names,
    "Marks": marks
})

print(df)

# Plot bar graph
plt.bar(df["Names"], df["Marks"], color='skyblue')

# Add labels
plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.title("Student Marks Bar Chart")

plt.show()