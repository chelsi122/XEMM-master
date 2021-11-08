import pandas as pd

def data_criptomonedas(data,exchanges):

    df = {'Exchanges':[],'dates':[],'levels':[],'bid':[],'ask':[],'volumenes':[],'mid_prices':[],'vwap':[]}


    for exchange in exchanges:
        for i in (data[exchange].keys()):
            #Obtener el exch
            exch= exchange
            df['Exchanges'].append(exch)

            #Sacar las fechas
            date= i
            Primerkey= pd.DataFrame(data[exchange][i])
            df['dates'].append(date)
            
            #Obtener los levels
            lev= len(Primerkey)
            df['levels'].append(lev)
            
            #Obtener los volumenes de bid y ask
            vol_bid= Primerkey.bid_size.sum()
            df['bid'].append(vol_bid)

            vol_ask= Primerkey.ask_size.sum()
            df['ask'].append(vol_ask)

            #Obtener el volumen total
            volume= vol_bid + vol_ask
            df['volumenes'].append(volume)

            #Obtener el midprice
            midprice= (Primerkey['ask'][0] + Primerkey['bid'][0])/2
            df['mid_prices'].append(midprice)

            #Obtener el VWAP
            VWAP_ask = (Primerkey.ask * Primerkey.ask_size).sum() / Primerkey.ask_size.sum()
            VWAP_bid = (Primerkey.bid * Primerkey.bid_size).sum() / Primerkey.bid_size.sum()
            VWAPT = (VWAP_ask + VWAP_bid)/2
            df['vwap'].append(VWAPT)

    
    
    return df