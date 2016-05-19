'''
Created on May 17, 2016
Problem
You want to make a dictionary that maps keys to more than one value (a so-called "multidict")
@author: Administrator
'''
prices = {
    'ACME':45.23,
    "AAPL":612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
}

if __name__ == '__main__':
    min_price = min(zip(prices.values(),prices.keys()))
    print 'min price is ',min_price
    max_price = max(zip(prices.values(),prices.keys()))
    print 'max_price is ',max_price
    prices_sorted = sorted(zip(prices.values(),prices.keys()))
    print prices_sorted