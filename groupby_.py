portfolio = [{'name': 'GOOG', 'shares': 50},
             {'name': 'YHOO', 'shares': 75},
             {'name': 'AOL', 'shares': 20},
             {'name': 'SCOX', 'shares': 65}]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
