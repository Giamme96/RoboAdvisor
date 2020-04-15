
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

    # mappa_strumenti = {
    #     "Stock" : ApiCallFromDictStock(),
    #     "ETF" : "Weekly",
    #     "Funds" : "Monthly"
    # }

    def AdjApiCall(self, symbol, periodicita, start):        #start convertibile in data

        # start = datetime(sy, sm, sd)
        endus = datetime.now()
        endeu = endus.strftime("%d/%m/%Y")
       

        # df = web.DataReader(symbol, self.mappa_periodicita[periodicita], start, end, api_key = self.key)
        df = inv.get_stock_historical_data(stock = symbol, country = "united states", from_date = start, to_date = endeu, as_json=False, order='ascending', interval = self.mappa_periodicita[periodicita])
        return df

    def ApiCallByIsin(self, isin, periodicita, start, tipologia_strumento):        

        # start = datetime(sy, sm, sd)
        endus = datetime.now()
        endeu = endus.strftime("%d/%m/%Y")
        country = CALC.GetCountryByIsin(isin)

        if tipologia_strumento == "Stock":

            stock = inv.stocks.get_stocks(country = country)
            by_isin_value_to_symbol = stock.loc[stock["isin"] == isin]["symbol"].values[0]

            df = inv.get_stock_historical_data(stock = by_isin_value_to_symbol, country = country, from_date = start, to_date = endeu, as_json=False, order='ascending', interval = self.mappa_periodicita[periodicita])
        
        elif tipologia_strumento == "ETF":

            etf = inv.etfs.get_etfs(country = country)
            by_isin_value_to_symbol = etf.loc[etf["isin"] == isin]["symbol"].values[0]

            df = inv.get_etf_historical_data(etf = by_isin_value_to_symbol, country = country, from_date = start, to_date = endeu, as_json=False, order='ascending', interval = self.mappa_periodicita[periodicita])

        # elif tipologia_strumento == "Fund":

        #     fund = inv.funds.get_funds(country = country)
        #     by_isin_value_to_symbol = fund.loc[fund["isin"] == isin]["symbol"].values[0]

        #     df = inv.get_fund_historical_data(fund = by_isin_value_to_symbol, country = country, from_date = start, to_date = endeu, as_json=False, order='ascending', interval = self.mappa_periodicita[periodicita])
        
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
    
    def ApiCallInfoStock(self, symbol): #restituisce le info della società

        info_stock = inv.stocks.get_stock_information(stock = symbol, country = "united states")

        return info_stock
        
    def ChiamataApiPortafoglioPanoramica(self): 

        # index_call = self.ApiIndexCallPortafoglio("nasdaq")  #chiamata all'indice per il calcolo del Beta
        
        for i in list(GLOBE.societa.keys()):

            if GLOBE.societa.get(i).get("daily_adj") == -1 and GLOBE.societa.get(i).get("df_info") == -1:

                datafetch = BEESCALLER().AdjApiCallPortafoglio(i)
                datafetch_info = BEESCALLER().ApiCallInfoStock(i)  #tipo dict
 
                # GLOBE.societa.get(i).get("daily_adj") = datafetch
                GLOBE.societa.get(i).update(daily_adj = datafetch)
                GLOBE.societa.get(i).update(df_info = datafetch_info)
                GLOBE.societa.get(i).update(totale_change = CALC.CalcoloChange(GLOBE.societa.get(i).get("daily_adj"), "Close", GLOBE.societa.get(i).get("price_ordine")))
                GLOBE.societa.get(i).update(beta = datafetch_info["Beta"].values[0])
                GLOBE.societa.get(i).update(one_year_change = datafetch_info["1-Year Change"].values[0])
                GLOBE.societa.get(i).update(currency = CALC.GetCurrency(GLOBE.societa.get(i).get("daily_adj")))
                print(f"Inserisco {i} nel dict societa.")

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

