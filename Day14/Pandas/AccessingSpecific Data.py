import pandas as pd

S = pd.Series([100, 200, 300, 400],
              index=["A", "B", "C", "D"])

# Access values B and D
result = S.loc[["B", "D"]]

print(result)