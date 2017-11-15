stocks = {
    'GOOG': 490.90,
    'FB': 67.0,
    'YHOO': 23.90,
    'AMZN': 306.89,
    'AAPL': 78.90
}

print(sorted(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(min(zip(stocks.values(), stocks.keys())))
