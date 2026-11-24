import pandas as pd

S1 = pd.Series([10, 20, 30],
               index=["apple", "banana", "cherry"])

S2 = pd.Series([5, 15, 25],
               index=["apple", "banana", "cherry"])

# Add both Series
result = S1 + S2

print(result)

# Total sales of all fruits
print("Total Sales:", result.sum())