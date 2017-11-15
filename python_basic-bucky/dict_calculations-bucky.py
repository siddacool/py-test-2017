stocks = {
    'BLA': 305,
    'CLU': 51,
    'GOOG': 110,
    'MICR': 208
}

min_price = min(zip(stocks.values(), stocks.keys()))

print(min_price)