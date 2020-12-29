import json
import numpy as np

with open('stock.json') as f:#open the file
    data = json.load(f)

class Position:

    def __init__(self, price=0, order=0, shares=0):
        self.shares = shares
        self.price = price
        self.order = order

    def position(self):
        print(order)
        if order == 'BUY':
            return -shares*price
        elif order == 'SELL':
            return shares*price
        elif order == 'CONFIRM':
            return 0
        elif order == 'CANCEL':
            return 0
            print('are you sure to cancel')
        else:
            return 0

Ticker = 'APPL'
newdic = dict()
position = []
for item in data['shares']:
    name = item['company']
    price = item['sharePrices']
    order = item['order']
    shares = item['NumberShares']
    newdic[name] = [price,order,shares]
print(newdic)


position = Position(newdic[Ticker])
print(position.position())

