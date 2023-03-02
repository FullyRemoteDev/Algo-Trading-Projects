import func_arbitrage

"""
    Step 0: Finding coins which can be traded
    Exchange: Poloniex
    API Docs: https://docs.legacy.poloniex.com/
"""

# Extract list of coins and prices from exchange
coin_json = func_arbitrage.get_coin_tickers('https://poloniex.com/public?command=returnTicker')

# Loop through each object and find the tradeable pairs
coin_list = func_arbitrage.collect_tradeables(coin_json)

print(len(coin_list))
print(len(coin_json))
