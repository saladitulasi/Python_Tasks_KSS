import pandas as pd

cities = {
    "Delhi": 2000000,
    "Mumbai": 3000000,
    "Chennai": 1500000
}

# Create Series with specified index
s = pd.Series(cities, index=["Delhi", "Chennai", "Bangalore"])

print(s)

# Identify missing values
print("\nMissing Values:")
print(s.isna())