
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
from datetime import timedelta
import investpy as inv

import pandas as pd
import pandas_datareader.data as web

import globalita as GLOBE
import Metodi_calcolo as CALC


class BEESCALLER():

    
    def ApiGetAllByIsin(self, isin, tipologia_strumento, periodicita, start):    #restituisce il nome di corrispondenza all'isin inserito

        country_iniziali = isin[:2]
        country = GLOBE.country_isin.get(country_iniziali)

        endus = datetime.now()
        endeu = endus.strftime("%d/%m/%Y")
        
        if tipologia_strumento == GLOBE.mappa_strumenti.get("Stock"):

            stock = inv.stocks.get_stocks(country = country)
            info_gen = stock.loc[stock["isin"] == isin]
            df = inv.get_stock_historical_data(stock = info_gen["symbol"].values[0], country = country, from_date = start, to_date = endeu, as_json=False, order='ascending', interval = GLOBE.mappa_periodicita[periodicita])

        elif tipologia_strumento == GLOBE.mappa_strumenti.get("ETF"):

            etf = inv.etfs.get_etfs(country = country)
            info_gen = etf.loc[etf["isin"] == isin]
            df = inv.get_etf_historical_data(etf = info_gen["name"].values[0], country = country, from_date = start, to_date = endeu, as_json=False, order='ascending', interval = GLOBE.mappa_periodicita[periodicita])
        
        elif tipologia_strumento == GLOBE.mappa_strumenti.get("Fund"):

            fund = inv.funds.get_funds(country = country)
            info_gen = fund.loc[fund["isin"] == isin]
            df = inv.get_fund_historical_data(fund = info_gen["name"].values[0], country = country, from_date = start, to_date = endeu, as_json=False, order='ascending', interval = GLOBE.mappa_periodicita[periodicita])
        
        all_info = {     #dict con tutte le informazioni
                    
            "datafetch" : df, 
            "info_gen" : info_gen, 
            "tipo_strumento" : tipologia_strumento
           }   

        return all_info
        
    def ApiGetAllByIsinPortafoglio(self, isin, tipologia_strumento):        

        years_obs = timedelta(days=365.24) * 5      
        endus = datetime.now()                      
        endeu = endus.strftime("%d/%m/%Y")          #conversioni date US a EU
        startus = endus - years_obs
        starteu = startus.strftime("%d/%m/%Y")

        country_iniziali = isin[:2]         #convertitore ISIN to country
        country = GLOBE.country_isin.get(country_iniziali)

        if tipologia_strumento == GLOBE.mappa_strumenti.get("Stock"):

            stock = inv.stocks.get_stocks(country = country)
            info_gen = stock.loc[stock["isin"] == isin]
            info_tech = inv.stocks.get_stock_information(info_gen["symbol"].values[0], country, as_json=False)
            df = inv.get_stock_historical_data(stock = info_gen["symbol"].values[0], country = country, from_date = starteu, to_date = endeu, as_json=False, order='ascending', interval = GLOBE.mappa_periodicita.get("Monthly"))

        elif tipologia_strumento == GLOBE.mappa_strumenti.get("ETF"):

            etf = inv.etfs.get_etfs(country = country)
            info_gen = etf.loc[etf["isin"] == isin]
            info_tech = inv.funds.get_fund_information(info_gen["name"].values[0], country, as_json=False)
            df = inv.get_etf_historical_data(etf = info_gen["name"].values[0], country = country, from_date = starteu, to_date = endeu, as_json=False, order='ascending', interval = GLOBE.mappa_periodicita.get("Monthly"))
        
        elif tipologia_strumento == GLOBE.mappa_strumenti.get("Fund"):

            fund = inv.funds.get_funds(country = country)
            info_gen = fund.loc[fund["isin"] == isin]
            info_tech = inv.etfs.get_etf_information(info_gen["name"].values[0], country, as_json=False)
            df = inv.get_fund_historical_data(fund = info_gen["name"].values[0], country = country, from_date = starteu, to_date = endeu, as_json=False, order='ascending', interval = GLOBE.mappa_periodicita.get("Monthly"))
        
        all_info_portafoglio = {  #dict con tutte le informazioni
               
            "datafetch" : df,
            "info_gen" : info_gen, 
            "info_tech" : info_tech, 
            "tipo_strumento" : tipologia_strumento
            }    

        return all_info_portafoglio
    
    # def ApiCallInfoStock(self, symbol): #restituisce le info della società

    #     info_stock = inv.stocks.get_stock_information(stock = symbol, country = "united states")

    #     return info_stock
        
    def ChiamataApiPortafoglioPanoramica(self): 

        # index_call = self.ApiIndexCallPortafoglio("nasdaq")  #chiamata all'indice per il calcolo del Beta
        
        for i in list(GLOBE.titolo.keys()):

            if GLOBE.titolo.get(i).get("dataframe") == -1:

                dataframe_dict = BEESCALLER().ApiGetAllByIsinPortafoglio(i, GLOBE.titolo.get(i).get("tipo_strumento"))
 
                GLOBE.titolo.get(i).update(dataframe = dataframe_dict)
                GLOBE.titolo.get(i).update(change_dall_acquisto = CALC.CalcoloChange(GLOBE.titolo.get(i).get("dataframe").get("datafetch"), "Close", GLOBE.titolo.get(i).get("price_ordine")))
                GLOBE.titolo.get(i).update(beta = dataframe_dict.get("info_tech")["Beta"].values[0])
                GLOBE.titolo.get(i).update(one_year_change = dataframe_dict.get("info_tech")["1-Year Change"].values[0])
                GLOBE.titolo.get(i).update(currency = dataframe_dict.get("info_gen")["currency"].values[0])
                print(f"Aggiorno il dict titolo.")
    