import heapq

grades = [67, 90, 78, 675, 21, 3]

print(heapq.nlargest(3, grades))

stocks = [
    {'ticker': 'BLA', 'price': 305},
    {'ticker': 'CLU', 'price': 51},
    {'ticker': 'GOOG', 'price': 110},
    {'ticker': 'MICR', 'price': 208}
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock['price']))