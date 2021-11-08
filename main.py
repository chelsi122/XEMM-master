
# -- --------------------------------------------------------------------------------------------------- -- #
# -- MarketMaker-BackTest                                                                                -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- file: main.py                                                                                       -- #
# -- Description: Main execution logic for the project                                                   -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- Author: IFFranciscoME - if.francisco.me@gmail.com                                                   -- #
# -- license: MIT License                                                                                -- #
# -- Repository: https://github.com/IFFranciscoME/MarketMaker-BackTest                                   -- #
# --------------------------------------------------------------------------------------------------------- #

# -- Load Packages for this script
import pandas as pd
import numpy as np
import pickle

# -- Load other scripts
from data import fees_schedule, order_book
from functions import data_criptomonedas
from visualizations import *

# Small test
exchanges = ['kraken','ftx','currencycom']  #'coinmate'
symbol_e = 'BTC/EUR' 
symbol_1 = 'DOGE/USD'
symbol_2 = 'LTC/USD'
symbol_3 = 'XRP/USD'

#DOT1-USD  BNB/USD

expected_volume = 0

# Get fee schedule
# fees = fees_schedule(exchange='kraken', symbol=symbol, expected_volume=expected_volume)


######################### DOGE/USD ###################################

# Massive download of OrderBook data
data_1 = order_book(symbol=symbol_1, exchanges=exchanges, output='inplace', stop=None, verbose=True)

# Guardar Diccionario
data_cripto1 = data_criptomonedas(data_1,exchanges)
dic_1 = open("dic_1.pkl", "wb")
pickle.dump(data_cripto1, dic_1)
dic_1.close()


data_DOGEUSD = pd.DataFrame(data_cripto1)

#Primera
graficas_DOGEUSD= grf_criptomonedas(data_DOGEUSD)
graficas_DOGEUSD.update_layout(title='Symbol DOG/USD')
graficas_DOGEUSD.show()


######################### LTC/USD ###################################

# Massive download of OrderBook data
data_2 = order_book(symbol=symbol_2, exchanges=exchanges, output='inplace', stop=None, verbose=True)

# Guardar Diccionario
data_cripto2 = data_criptomonedas(data_2,exchanges)
dic_2 = open("dic_2.pkl", "wb")
pickle.dump(data_cripto2, dic_2)
dic_2.close()


data_LTCUSD = pd.DataFrame(data_cripto2)

#Primera
graficas_LTCUSD= grf_criptomonedas(data_LTCUSD)
graficas_LTCUSD.update_layout(title='Symbol DOG/USD')
graficas_LTCUSD.show()

######################### XRP/USD ###################################

# Massive download of OrderBook data
data_3 = order_book(symbol=symbol_3, exchanges=exchanges, output='inplace', stop=None, verbose=True)

# Guardar Diccionario
data_cripto3 = data_criptomonedas(data_3,exchanges)
dic_3 = open("dic_3.pkl", "wb")
pickle.dump(data_cripto3, dic_3)
dic_3.close()


data_XRPUSD = pd.DataFrame(data_cripto2)

#Primera
graficas_XRPUSD= grf_criptomonedas(data_XRPUSD)
graficas_XRPUSD.update_layout(title='Symbol XRP/USD')
graficas_XRPUSD.show()




# Test
# data['kraken'][list(data['kraken'].keys())[2]]

# Read previously downloaded file
ob_data = pd.read_json('files/orderbooks_06jun2021.json', orient='values', typ='series')

# -- Simulation of trades (Pending)

"""
- Type A: Make a BID in Kraken, then Take BID in Bitfinex

Check Signal_BID
    Difference between BIDs on Origin and Destination is greater than Maker_Margin_BID
    Make on Destination and Take on Origin

kr_maker_bid * (1 + kr_maker_fee) = bf_taker_bid * (1 - bf_taker_fee)
e.g. -> 5942.5638 * (1 + 0.0016) = 5964.00 * (1 - 0.0020) = 0

- Type B: Take an ASK on Bitfinex, then Make an ASK in Kraken

Check Signal_ASK
    Difference between ASKs on Origin and Destination is greater than Maker_Margin_ASK
    Take on Origin and Maker on Destination

bf_taker_ask * (1 + bf_taker_fee) = kr_maker_ask * (1 - kr_maker_fee)
e.g. -> 6000 * (1 + 0.0020) - 6021.6346 * (1 - 0.0016) = 0
"""
