from datetime import datetime
import json
import tkinter as tk
import Metodi_calcolo as CALC
import API_call as CALLAPI
import Lavoro_file as FILE

titolo = {}    

country_isin = {            #da completare con tutti i riferimenti
        "US" : "united states",
        "IT" : "italy",
        "GB" : "great britain"
    }

mappa_strumenti = {

        "Stock" : "stock",
        "ETF" : "etf",
        "Fund" : "fund"
    }

mappa_periodicita = {

        "Daily" : "daily",
        "Weekly" : "weekly",
        "Monthly" : "monthly"
    }
    
def AggiungiTitolo(isin, nome, symbol, tipologia_strumento, country, quantita, position, date, price, dataframe_dict):

    Titolo_dict = {

        "isin" : isin,
        "nome": nome,
        "symbol" : symbol,
        "tipo_strumento" : tipologia_strumento,
        "country" : country,
        "quantity" : quantita,
        "position" : position,
        "beta" : CALC.GetItemFromInfoTech(dataframe_dict, tipologia_strumento, "Beta"),  
        "data_ordine" : date,
        "price_ordine" : price,
        "totale_ordine" : price * quantita,
        "change_dall_acquisto" : CALC.CalcoloChange(dataframe_dict, price),
        "one_year_change" : CALC.GetItemFromInfoTech(dataframe_dict, tipologia_strumento, "1-Year Change"),
        "currency" : CALC.GetCurrencyFromInfoGen(dataframe_dict),
        "dataframe" : dataframe_dict   #da tenere per ultimo per la costruzione della tabella
        
    }

    global titolo 
    
    titolo[isin] = Titolo_dict     
    
def MenuTitoliPortafoglioModifica():     

    array_titoli = []
    
    for item in titolo.values():

        array_titoli.append(item.get("nome"))  #aggiunge un nuovo elemento item all'array
        
    return array_titoli



