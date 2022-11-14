from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp

coingecko = CoinGeckoAPI()

def get_data(cryptocurrency):
    cryptocurrency_data = coingecko.get_coin_by_id(cryptocurrency, market_data='true', sparkline='true')
    df = pd.DataFrame.from_dict(cryptocurrency_data, orient='index')
    df.to_csv(r'cryptocurrency_data.csv')
    return df

def get_historical_data(cryptocurrency, fiat_currency, number_of_days):
    historic_price = coingecko.get_coin_market_chart_by_id(cryptocurrency, fiat_currency, number_of_days)
    prices = [price[1] for price in historic_price['prices']]
    return prices

ethereum = get_historical_data('ethereum', 'USD', 30)
et_df = pd.DataFrame(ethereum, columns = ['Ethereum Value'])
et_df.index.name = 'Every Hour Count in the Past 30 Days'
et_df.to_csv(r'Ethereum.csv')
df = pd.read_csv("Ethereum.csv")


