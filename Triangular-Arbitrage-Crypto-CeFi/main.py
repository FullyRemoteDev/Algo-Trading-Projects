import requests
import json

"""
    Step 0: Finding coins which can be traded
    Exchange: Poloniex
    API Docs: https://docs.legacy.poloniex.com/
"""

# Extract list of coins and prices from exchange
url = 'https://poloniex.com/public?command=returnTicker'
req = requests.get(url)
coin_json = json.loads(req.text)

# Loop through each object and find the tradeable pairs
for coin in coin_json:
    is_frozen = coin_json[coin]['isFrozen']
    is_post_only = coin_json[coin]['postOnly']
    if is_frozen != '0' or is_post_only != '0':
        print(coin, is_frozen, is_post_only)

