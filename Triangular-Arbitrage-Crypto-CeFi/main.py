import json

import func_arbitrage


# Set variables
coin_price_url = 'https://poloniex.com/public?command=returnTicker'

def step_0():
    """
        Step 0: Finding coins which can be traded
        Exchange: Poloniex
        API Docs: https://docs.legacy.poloniex.com/
    """

    # Extract list of coins and prices from exchange
    coin_json = func_arbitrage.get_coin_tickers(coin_price_url)

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


def step_2():
    """
        Step 2: Calculate Surface Arbitrage Opportunities
        Exchange: Poloniex
        API Docs: https://docs.legacy.poloniex.com/
    """

    # Get Structured Pairs
    with open("structure_triangular_pairs.json") as json_file:
        structured_pairs = json.load(json_file)

    # Get Latest Surface Prices
    prices_json = func_arbitrage.get_coin_tickers(coin_price_url)

    # Loop through and Structure Price Information
    for t_pair in structured_pairs:
        prices_dict = func_arbitrage.get_price_for_t_pair(t_pair, prices_json)
        surface_arb = func_arbitrage.calc_triangular_arb_surface_rate(t_pair, prices_dict)


""" MAIN """
if __name__ == "__main__":
    # coin_list = step_0()
    # structured_pairs = step_1(coin_list)
    step_2()

