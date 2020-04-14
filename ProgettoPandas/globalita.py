from datetime import datetime
import json
import tkinter as tk
import Metodi_calcolo as CALC
import API_call as CALLAPI

societa = {}    

lista_NASDAQ = {}

def CaricaNASDAQ():

    with open('ProgettoPandas/NASDAQ.json') as json_file:

        data = json.load(json_file)
        for i in data:
            
            lista_NASDAQ[i["Company Name"]] = i["Symbol"]

def AggiungiSocieta(nome, quantita, position, date, price, datafetch, datafetch_info):

    symbol = lista_NASDAQ.get(nome)

    NewCo = {
        "nome" : nome,
        "symbol" : symbol,
        "quantity" : quantita,
        "position" : position,
        "beta" : CALC.GetFromDfToSocieta(datafetch_info, "Beta"),  
        "data_ordine" : date,
        "price_ordine" : price,
        "totale_ordine" : price * quantita,
        "totale_change" : CALC.CalcoloChange(datafetch, "Close", price),
        "one_year_change" : CALC.GetFromDfToSocieta(datafetch_info, "1-Year Change"),
        "currency" : CALC.GetCurrency(datafetch),
        "daily_adj" : datafetch,     #da tenere per ultimo per la costruzione della tabella
        "df_info" : datafetch_info
    }

    global societa 
    
    societa[symbol] = NewCo     
    
def CheckListaModPortafoglio():     

    array_societa = []
    
    for item in societa.values():

        array_societa.append(item.get("nome"))  #aggiunge un nuovo elemento item all'array
        
    return array_societa





