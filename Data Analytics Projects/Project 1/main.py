# Railway Gauge Analysis Using Python
# Keep this .py file and "railway_gauges 1.csv" in the same folder.

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the CSV file
df = pd.read_csv("railway_gauges 1.csv")

# 2. Display basic information
print("FIRST FIVE ROWS")
print(df.head())

print("\nDATASET INFORMATION")
print(df.info())

print("\nSTATISTICAL SUMMARY")
print(df.describe())

# 3. Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# 4. Convert gauge columns to numeric values
gauge_cols = ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
for col in gauge_cols + ["Total"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 5. Line graph: compare all gauge types over the years
plt.figure(figsize=(12, 6))
for col in gauge_cols:
    plt.plot(df["Year"], df[col], marker="o", label=col)
plt.title("Railway Gauge Lengths Over the Years")
plt.xlabel("Year")
plt.ylabel("Track Length (dataset values)")
plt.xticks(rotation=70)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 6. Line graph: total railway track length
plt.figure(figsize=(12, 5))
plt.plot(df["Year"], df["Total"], marker="o")
plt.title("Total Railway Track Length Over the Years")
plt.xlabel("Year")
plt.ylabel("Total (dataset values)")
plt.xticks(rotation=70)
plt.grid(True)
plt.tight_layout()
plt.show()

# 7. Bar graph: compare gauge types in the latest year
latest = df.iloc[-1]
plt.figure(figsize=(8, 5))
plt.bar(gauge_cols, [latest[col] for col in gauge_cols])
plt.title("Gauge-wise Comparison in " + str(latest["Year"]))
plt.xlabel("Gauge Type")
plt.ylabel("Track Length (dataset values)")
plt.tight_layout()
plt.show()

# 8. Pie chart: share of each gauge across all records
gauge_totals = df[gauge_cols].sum()
plt.figure(figsize=(7, 7))
plt.pie(gauge_totals, labels=gauge_totals.index, autopct="%1.1f%%")
plt.title("Share of Each Gauge Across All Yearly Records")
plt.show()

# 9. Find maximum and minimum values
print("\nMAXIMUM AND MINIMUM VALUES")
for col in gauge_cols + ["Total"]:
    max_row = df.loc[df[col].idxmax()]
    min_row = df.loc[df[col].idxmin()]
    print(f"\n{col}")
    print("Maximum:", max_row[col], "in", max_row["Year"])
    print("Minimum:", min_row[col], "in", min_row["Year"])

# 10. Save analyzed data
df.to_csv("railway_gauge_analyzed.csv", index=False)
print("\nAnalysis completed. Output saved as railway_gauge_analyzed.csv")
