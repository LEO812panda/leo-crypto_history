from pycoingecko import CoinGeckoAPI
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
from datetime import datetime, date

coingecko = CoinGeckoAPI()

def get_data(cryptocurrency):
    cryptocurrency_data = coingecko.get_coin_by_id(cryptocurrency, market_data='true', sparkline='true')
    df = pd.DataFrame.from_dict(cryptocurrency_data, orient='index')
    # df.to_csv(r'cryptocurrency_data.csv')
    return df

def get_historical_data(cryptocurrency, fiat_currency, number_of_days):
    historic_price = coingecko.get_coin_market_chart_by_id(cryptocurrency, fiat_currency, number_of_days, interval="daily")
    prices = [price[1] for price in historic_price['prices']]
    date = [datetime.utcfromtimestamp(x[0]/1000).date() for x in historic_price['prices'] ]
    return prices, date

from tkinter import *

top = Tk()

E1 = Entry(top, bd =5)
E1.pack(side = LEFT)

E2 = Entry(top, bd =6)
E2.pack(side = RIGHT)

historyData=[]
def CallBack():
    historyData, tt=get_historical_data(E1.get(), 'USD', int(E2.get())-1)
    total = []
    total = pd.DataFrame(total)
    total['date'] = tt
    total['price'] = historyData    
    total.to_csv(E1.get()+'.csv')
    return total

B = Button(top, text ="Save", command = CallBack)
B.pack()
top.mainloop()