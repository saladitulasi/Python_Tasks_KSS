import pandas as pd

df = pd.DataFrame({
    "Price": [100, 200, 300]
})

# Add Discount column (10%)
df["Discount"] = df["Price"] * 0.10

# Add Final Price column
df["Final Price"] = df["Price"] - df["Discount"]

print(df)