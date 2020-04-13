
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
from datetime import timedelta
import investpy as inv

import pandas as pd
import pandas_datareader.data as web

import globalita as GLOBE
import Metodi_calcolo as CALC


class BEESCALLER():

    key = 'OQ5SXA6KT34O569F'
    api = 0

    mappa_periodicita = {
        "Daily" : "Daily",
        "Weekly" : "Weekly",
        "Monthly" : "Monthly"
    }

    def AdjApiCall(self, symbol, periodicita, start):        #start convertibile in data

        # start = datetime(sy, sm, sd)
        endus = datetime.now()
        endeu = endus.strftime("%d/%m/%Y")
       

        # df = web.DataReader(symbol, self.mappa_periodicita[periodicita], start, end, api_key = self.key)
        df = inv.get_stock_historical_data(stock = symbol, country = "united states", from_date = start, to_date = endeu, as_json=False, order='ascending', interval = self.mappa_periodicita[periodicita])
        return df

    def AdjApiCallPortafoglio(self, symbol):        #call all'api da inserire nel portafoglio ultime 60 obs.

        years_obs = timedelta(days=365.24) * 5      
        endus = datetime.now()                      
        endeu = endus.strftime("%d/%m/%Y")          #conversioni date US a EU
        startus = endus - years_obs
        starteu = startus.strftime("%d/%m/%Y")
      
        # dfp = web.DataReader(symbol, self.mappa_periodicita["Monthly"], start, endeu, api_key = self.key)
        dfp = inv.get_stock_historical_data(stock = symbol, country = "united states", from_date = starteu, to_date = endeu, as_json = False, order = 'ascending', interval = self.mappa_periodicita.get("Monthly"))
        print(f"Call API portafoglio {symbol}")

        return dfp
        
    def ChiamataApiPortafoglioPanoramica(self): 

        index_call = self.ApiIndexCallPortafoglio("nasdaq")  #chiamata all'indice per il calcolo del Beta
        
        for i in list(GLOBE.societa.keys()):

            if GLOBE.societa.get(i).get("daily_adj") == -1:

                datafetch = BEESCALLER().AdjApiCallPortafoglio(i)

                # GLOBE.societa.get(i).get("daily_adj") = datafetch
                GLOBE.societa.get(i).update(daily_adj = datafetch)
                GLOBE.societa.get(i).update(totale_change = CALC.CalcoloChange(GLOBE.societa.get(i).get("daily_adj"), "Close", GLOBE.societa.get(i).get("price_ordine")))
                GLOBE.societa.get(i).update(beta = CALC.RegressioneBetaPortafoglio(GLOBE.societa.get(i).get("daily_adj"), index_call))
                GLOBE.societa.get(i).update(currency = CALC.GetCurrency(GLOBE.societa.get(i).get("daily_adj")))
                print(f"Inserisco {i} perchè non c'erano i dati.")

    def ApiIndexCallPortafoglio(self, index_symbol):      #TODO da implementare nel caso vengano scelti per il portafoglio titoli diversi dal paniere nasdaq per fare la regressione
                                                            #restituisce il datafetch raw
        years_obs = timedelta(days=365.24) * 5      
        endus = datetime.now()                      
        endeu = endus.strftime("%d/%m/%Y")          #conversioni date US a EU
        startus = endus - years_obs
        starteu = startus.strftime("%d/%m/%Y")
      
        dfindex = inv.get_index_historical_data(index = index_symbol, country = 'united states', from_date = starteu , to_date = endeu, as_json = False, order = 'ascending', interval = self.mappa_periodicita.get("Monthly"))
        print(f"Api index : {index_symbol}")

        return dfindex      

