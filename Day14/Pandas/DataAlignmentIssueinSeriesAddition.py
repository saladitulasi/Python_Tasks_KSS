import pandas as pd

S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])

S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])

# Add both Series
result = S1 + S2

print("Addition of Series:")
print(result)

# Replace NaN with 0
final_result = S1.add(S2, fill_value=0)

print("\nFinal Result:")
print(final_result)

# Calculate total
print("\nTotal:", final_result.sum())