import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create temperature data
temps = np.array([28, 30, 32, 31, 29])

# Convert into Pandas Series
temperature = pd.Series(temps)

print(temperature)

# Plot line graph
temperature.plot(marker='o', color='red')

# Add title and grid
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.show()