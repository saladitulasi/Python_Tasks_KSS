prices = [100, 200, 300, 400]

updated_prices = [p * 0.9 if p > 200 else p for p in prices]

print("Original Prices:", prices)
print("Updated Prices:", updated_prices)