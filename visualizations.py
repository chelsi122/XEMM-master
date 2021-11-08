
# -- --------------------------------------------------------------------------------------------------- -- #
# -- MarketMaker-BackTest                                                                                -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- file: visualizations.py                                                                             -- #
# -- Description: Functions for plots, tables and text visualizations for the project                    -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- Author: IFFranciscoME - if.francisco.me@gmail.com                                                   -- #
# -- license: MIT License                                                                                -- #
# -- Repository: https://github.com/IFFranciscoME/MarketMaker-BackTest                                   -- #
# --------------------------------------------------------------------------------------------------------- #

# -- Load base packages
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from rich import inspect

def grf_criptomonedas(data_cripto):

    ################## Número de Niveles #######################
    fig = make_subplots(3, 2, x_title= 'Fechas', y_title='Cantidad', 
    subplot_titles=('Niveles','Volumen Bid', 'Volumen Ask','Volumen','Mid-prices','VWAP'))

    ### kraken
    data_kraken= data_cripto[data_cripto['Exchanges']=='kraken']
    niveles_k = data_kraken['levels'].tolist()
    vol_bid_k= data_kraken['bid'].tolist()
    vol_ask_k= data_kraken['ask'].tolist()
    vol_T_k = data_kraken['volumenes'].tolist()
    mid_prices_k = data_kraken['mid_prices'].tolist()
    vwap_k= data_kraken['vwap'].tolist()
    fechas_k = data_kraken['dates'].tolist()

    ### ftx
    data_ftx= data_cripto[data_cripto['Exchanges']=='ftx']
    niveles_ftx = data_ftx['levels'].tolist()
    vol_bid_ftx= data_ftx['bid'].tolist()
    vol_ask_ftx= data_ftx['ask'].tolist()
    vol_T_ftx= data_ftx['volumenes'].tolist()
    mid_prices_ftx= data_ftx['mid_prices'].tolist()
    vwap_ftx= data_ftx['vwap'].tolist()
    fechas_ftx = data_ftx['dates'].tolist()

    ### currencycom
    data_curr= data_cripto[data_cripto['Exchanges']=='currencycom']
    niveles_curr = data_curr['levels'].tolist()
    vol_bid_curr = data_curr['bid'].tolist()
    vol_ask_curr = data_curr['ask'].tolist()
    vol_T_curr = data_curr['volumenes'].tolist()
    mid_prices_curr = data_curr['mid_prices'].tolist()
    vwap_curr = data_curr['vwap'].tolist()
    fechas_curr = data_curr['dates'].tolist()

    ### coinmate
    data_coi= data_cripto[data_cripto['Exchanges']=='coinmate']
    niveles_coi = data_coi['levels'].tolist()
    vol_bid_coi = data_coi['bid'].tolist()
    vol_ask_coi = data_coi['ask'].tolist()
    vol_T_coi = data_coi['volumenes'].tolist()
    mid_prices_coi = data_coi['mid_prices'].tolist()
    vwap_coi = data_coi['vwap'].tolist()
    fechas_coi = data_coi['dates'].tolist()

   

    ##### Niveles ##########

    ## kraken
    fig.add_trace(go.Scatter(x= fechas_k, y= niveles_k, name='Número de Niveles Kraken',
                            line=dict(color='darkslategray', width=4)),1,1)

    ## ftx
    fig.add_trace(go.Scatter(x=fechas_ftx, y=niveles_ftx, name = 'Número de Niveles Ftx',
                            line=dict(color='teal', width=4)),1,1)
    
    ## Currencycom
    fig.add_trace(go.Scatter(x=fechas_curr, y=niveles_curr, name='Número de Niveles Currencycom',
                            line=dict(color='lightseagreen', width=4,
                                dash='dash')),1,1)

    ##Coinmate
    fig.add_trace(go.Scatter(x=fechas_coi, y=niveles_coi, name='Número de Niveles Total Coinmate',
                            line=dict(color='aquamarine', width=4,
                                dash='dash')),1,1)

    ##### Volumen bid ##########

    ##kraken
    fig.add_trace(go.Scatter(x=fechas_k, y=vol_bid_k, name='Volumen de bid Kraken',
                            line=dict(color='darkslategray', width=4)),1,2)

    ## Ftx
    fig.add_trace(go.Scatter(x=fechas_ftx, y=vol_bid_ftx, name = 'Volumen de bid Ftx',
                            line=dict(color='teal', width=4)),1,2)

    ##Currencycom
    fig.add_trace(go.Scatter(x=fechas_curr, y=vol_bid_curr, name='Volumen de bid Currencycom',
                            line=dict(color='lightseagreen', width=4,
                                dash='dash')),1,2)

    ##Coinmate
    fig.add_trace(go.Scatter(x=fechas_coi, y=vol_bid_coi, name='Volumen de bid Coinmate',
                            line=dict(color='aquamarine', width=4,
                                dash='dash')),1,2)

    ##### Volumen ask ##########

    # kraken
    fig.add_trace(go.Scatter(x=fechas_k, y=vol_ask_k, name='Volumen de ask Kraken',
                            line=dict(color='darkslategray', width=4)),2,1)

    fig.add_trace(go.Scatter(x=fechas_ftx, y=vol_ask_ftx, name = 'Volumen de ask Ftx',
                            line=dict(color='teal', width=4)),2,1)

    fig.add_trace(go.Scatter(x=fechas_curr, y=vol_ask_curr, name='Volumen de ask Currencycom',
                            line=dict(color='lightseagreen', width=4,
                                dash='dash')),2,1)

    fig.add_trace(go.Scatter(x=fechas_coi, y=vol_ask_coi, name='Volumen de ask Coinmate',
                            line=dict(color='aquamarine', width=4,
                                dash='dash')),2,1)
    
    ##### Volumen Total ##########
    
    # kraken
    fig.add_trace(go.Scatter(x=fechas_k, y=vol_T_k, name='Volumen Total Kraken',
                            line=dict(color='darkslategray', width=4)),2,2)

    fig.add_trace(go.Scatter(x=fechas_ftx, y=vol_T_ftx, name = 'Volumen Total Ftx',
                            line=dict(color='teal', width=4)),2,2)

    fig.add_trace(go.Scatter(x=fechas_curr, y=vol_T_curr, name='Volumen Total Currencycom',
                            line=dict(color='lightseagreen', width=4,
                                dash='dash')),2,2)

    fig.add_trace(go.Scatter(x=fechas_coi, y=vol_T_coi, name='Volumen Total Coinmate',
                            line=dict(color='aquamarine', width=4,
                                dash='dash')),2,2)

    ##### Mid price #########

    # kraken
    fig.add_trace(go.Scatter(x=fechas_k, y=mid_prices_k, name='Mid-price Kraken',
                            line=dict(color='darkslategray', width=4)),3,1)

    fig.add_trace(go.Scatter(x=fechas_ftx, y=mid_prices_ftx, name = 'Mid-price Ftx',
                            line=dict(color='teal', width=4)),3,1)

    fig.add_trace(go.Scatter(x=fechas_curr, y=mid_prices_curr, name='Mid-price Currencycom',
                            line=dict(color='lightseagreen', width=4,
                                dash='dash')),3,1)

    fig.add_trace(go.Scatter(x=fechas_coi, y=mid_prices_coi, name='Mid-price Coinmate',
                            line=dict(color='aquamarine', width=4,
                                dash='dash')),3,1)

     ##### VWAP #########

     # kraken
    fig.add_trace(go.Scatter(x=fechas_k, y= vwap_k, name='VWAP Kraken',
                            line=dict(color='darkslategray', width=4)),3,2)

    fig.add_trace(go.Scatter(x=fechas_ftx, y= vwap_ftx, name = 'VWAP Ftx',
                            line=dict(color='teal', width=4)),3,2)

    fig.add_trace(go.Scatter(x=fechas_curr, y= vwap_curr, name='VWAP Currencycom',
                            line=dict(color='lightseagreen', width=4,
                                dash='dash')),3,2)

    fig.add_trace(go.Scatter(x=fechas_coi, y= vwap_coi, name='VWAP Coinmate',
                            line=dict(color='aquamarine', width=4,
                                dash='dash')),3,2)

    return fig