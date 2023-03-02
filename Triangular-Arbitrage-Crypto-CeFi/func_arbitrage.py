import requests
import json


# Make a GET request
def get_coin_tickers(url):
    req = requests.get(url)
    json_response = json.loads(req.text)
    return json_response


# Loop through each object and find the tradeable pairs
def collect_tradeables(json_object):
    coin_list = []
    for coin in json_object:
        is_frozen = json_object[coin]['isFrozen']
        is_post_only = json_object[coin]['postOnly']
        if is_frozen == '0' and is_post_only == '0':
            coin_list.append(coin)
    return coin_list
