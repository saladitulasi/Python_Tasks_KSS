
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Temperature data
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Create DataFrame
df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

print("Temperature Data:")
print(df)

# 1. Line Graph
plt.figure(figsize=(6, 4))
plt.plot(days, temps, marker='o', color='blue')
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# 2. Bar Chart
plt.figure(figsize=(6, 4))
plt.bar(days, temps, color='green')
plt.title("Day-wise Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.show()

# 3. Pie Chart - High vs Low temperature
high = np.sum(temps > 30)
low = np.sum(temps <= 30)

plt.figure(figsize=(6, 4))
plt.pie(
    [high, low],
    labels=["High Temperature", "Low Temperature"],
    autopct='%1.1f%%',
    colors=['tomato', 'skyblue']
)
plt.title("High vs Low Temperature")
plt.show()

# 4. Histogram
plt.figure(figsize=(6, 4))
plt.hist(temps, bins=5, color='orange', edgecolor='black')
plt.title("Temperature Frequency")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(range(len(temps)), temps, color='red')
plt.title("Day Index vs Temperature")
plt.xlabel("Day Index")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
