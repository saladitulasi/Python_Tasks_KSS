import pandas as pd

data = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Math": [80, 70, 60],
    "Science": [90, 60, 70]
})

# Add Total column
data["Total"] = data["Math"] + data["Science"]

print(data)

# Find student with highest total marks
highest = data.loc[data["Total"].idxmax()]

print("\nStudent with Highest Marks:")
print(highest)