import json

import func_arbitrage


def step_0():
    """
        Step 0: Finding coins which can be traded
        Exchange: Poloniex
        API Docs: https://docs.legacy.poloniex.com/
    """

    # Extract list of coins and prices from exchange
    coin_json = func_arbitrage.get_coin_tickers('https://poloniex.com/public?command=returnTicker')

    # Loop through each object and find the tradeable pairs
    coin_list = func_arbitrage.collect_tradeables(coin_json)

    # Return list of tradeable coins
    return coin_list


def step_1(coin_list):
    """
        Step : Structuring Triangular Pairs
        Calculation Only
    """

    # Structure the list of tradeable triangular arbitrage pairs
    structured_list = func_arbitrage.structure_triangular_pairs(coin_list)

    # Save structured list
    with open("structure_triangular_pairs.json", "w") as fp:
        json.dump(structured_list, fp)


""" MAIN """
if __name__ == "__main__":
    coin_list = step_0()
    structured_pairs = step_1(coin_list)

