import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create data
scores = np.array([40, 60, 80, 30, 90])

# Categorize scores
pass_count = np.sum(scores > 50)
fail_count = np.sum(scores <= 50)

# Create DataFrame
df = pd.DataFrame({
    "Result": ["Pass", "Fail"],
    "Count": [pass_count, fail_count]
})

print(df)

# Plot pie chart
plt.pie(
    df["Count"],
    labels=df["Result"],
    autopct='%1.1f%%',
    colors=['green', 'red']
)

plt.title("Pass vs Fail Distribution")

plt.show()