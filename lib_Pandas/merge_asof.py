import pandas as pd

# Create Stock Prices DataFrame
stock_prices = pd.DataFrame({
    'date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']),
    'price': [100, 102, 105, 103, 108]
})

# Create Economic Indicators DataFrame
economic_indicators = pd.DataFrame({
    'date': pd.to_datetime(['2024-01-01', '2024-01-03', '2024-01-05']),
    'gdp': [1.5, 1.7, 1.8]
})

# Perform asof merge
merged_data = pd.merge_asof(stock_prices, economic_indicators, on='date')