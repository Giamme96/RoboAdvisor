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

def AggiungiSocieta(nome, quantita, position, date, price, datafetch):

    symbol = lista_NASDAQ.get(nome)

    NewCo = {
        "nome" : nome,
        "symbol" : symbol,
        "quantity" : quantita,
        "position" : position,
        "beta" : CALC.RegressioneBetaPortafoglio(datafetch, CALLAPI.BEESCALLER().ApiIndexCallPortafoglio("nasdaq")),   #TODO index solo nasdaq
        "data_ordine" : date,
        "price_ordine" : price,
        "totale_ordine" : price * quantita,
        "totale_change" : CALC.CalcoloChange(datafetch, "Close", price),
        "currency" : CALC.GetCurrency(datafetch),
        "daily_adj" : datafetch     #da tenere per ultimo per la costruzione della tabella
        
    }

    global societa 
    
    societa[symbol] = NewCo     
    
def CheckListaModPortafoglio():     

    array_societa = []
    
    for item in societa.values():

        array_societa.append(item.get("nome"))  #aggiunge un nuovo elemento item all'array
        
    return array_societa





