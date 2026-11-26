import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]

# Convert into DataFrame
df = pd.DataFrame({
    "Months": months,
    "Sales": sales
})

print(df)

# Plot line graph
plt.plot(df["Months"], df["Sales"], marker='o')

# Add labels
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales")

plt.show()