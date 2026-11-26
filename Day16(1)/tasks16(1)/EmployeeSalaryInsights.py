
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Employee salary data
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

# Create DataFrame
df = pd.DataFrame({
    "Department": departments,
    "Salary": salaries
})

print("Employee Salary Data:")
print(df)

# 1. Line Graph
plt.figure(figsize=(6, 4))
plt.plot(range(len(salaries)), salaries, marker='o', color='blue')
plt.title("Salary Trend")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# 2. Bar Chart - Department-wise salary
dept_salary = df.groupby("Department")["Salary"].mean()

plt.figure(figsize=(6, 4))
plt.bar(dept_salary.index, dept_salary.values, color='green')
plt.title("Department-wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# 3. Pie Chart - Department distribution
dept_count = df["Department"].value_counts()

plt.figure(figsize=(6, 4))
plt.pie(dept_count, labels=dept_count.index,
        autopct='%1.1f%%')
plt.title("Department Distribution")
plt.show()

# 4. Histogram - Salary distribution
plt.figure(figsize=(6, 4))
plt.hist(salaries, bins=5, color='orange', edgecolor='black')
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot - Index vs Salary
plt.figure(figsize=(6, 4))
plt.scatter(range(len(salaries)), salaries, color='red')
plt.title("Employee Index vs Salary")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.grid(True)
plt.show()
