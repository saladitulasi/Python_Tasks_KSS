
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student marks
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

# Create DataFrame
df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

print("Student Performance Data:")
print(df)

# 1. Line Graph
plt.figure(figsize=(6, 4))
plt.plot(students, marks, marker='o', color='blue')
plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# 2. Bar Chart
plt.figure(figsize=(6, 4))
plt.bar(students, marks, color='green')
plt.title("Student vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Pie Chart (Pass vs Fail)
passed = np.sum(marks > 50)
failed = np.sum(marks <= 50)

plt.figure(figsize=(6, 4))
plt.pie(
    [passed, failed],
    labels=["Pass", "Fail"],
    autopct='%1.1f%%',
    colors=['lightgreen', 'lightcoral']
)
plt.title("Pass vs Fail")
plt.show()

# 4. Histogram
plt.figure(figsize=(6, 4))
plt.hist(marks, bins=5, color='orange', edgecolor='black')
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(range(len(marks)), marks, color='red')
plt.title("Index vs Marks")
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
