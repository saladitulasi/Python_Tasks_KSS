import pandas as pd
import matplotlib.pyplot as plt

# Create data
data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Store_A": [100, 150, 200],
    "Store_B": [90, 140, 210]
}

# Create DataFrame
df = pd.DataFrame(data)

print(df)

# Plot two line graphs
plt.plot(df["Month"], df["Store_A"],
         marker='o', label="Store A")

plt.plot(df["Month"], df["Store_B"],
         marker='o', label="Store B")

# Add labels and title
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales Comparison")

# Add legend
plt.legend()

plt.show()