
import json
from datetime import datetime

import globalita as GLOBE
import API_call as CALLAPI

def ScritturaPortFile():

    jsonfile = {}
    for i in GLOBE.societa:

        temp = {
            "nome" : GLOBE.societa.get(i).get("nome"),
            "symbol" : GLOBE.societa.get(i).get("symbol"),
            "quantity" : GLOBE.societa.get(i).get("quantity"),
            "position" : GLOBE.societa.get(i).get("position"),
            "data_ordine" : datetime.strftime(GLOBE.societa.get(i).get("data_ordine"), '%Y-%m-%d %H:%M:%S.%f'),
            "price_ordine" : GLOBE.societa.get(i).get("price_ordine"),
            "totale_ordine" : GLOBE.societa.get(i).get("totale_ordine"),
            "totale_change" : GLOBE.societa.get(i).get("totale_change"),
            "currency" : GLOBE.societa.get(i).get("currency")
        }

        jsonfile[GLOBE.societa.get(i).get("symbol")] = temp
    
# jsonfile = {symbol : {"Price" : dfp["adjusted close"].iloc[len(dfp) - 1], "Quantity" : self.quantity_agg.get(), "Position" : self.position_agg.get(), "Date" : str(datetime.now())}}

    with open("Portafoglio.json", "w") as outfile:

        json.dump(jsonfile, outfile)

def LetturaPortFile():

    with open('Portafoglio.json') as json_file:

        data = json.load(json_file)
                
        for i in data:
        
            GLOBE.AggiungiSocieta(data.get(i).get("nome"), data.get(i).get("quantity"), data.get(i).get("position"), datetime.strptime(data.get(i).get("data_ordine"), '%Y-%m-%d %H:%M:%S.%f'), data.get(i).get("price_ordine"), -1, -1)

def ScritturaProfilazione():    #la posizione dell'utente investitore

    json_profilazione = {

        "classificazione_rischio" : "speculazione"  #speculazione, risparmio, crescita capitale

    }

    with open("Profilazione.json", "w") as outfile:

        json.dump(json_profilazione, outfile)

def LetturaProfilazione():  #da utilizzare la profilazione dell'investitore per permettere alcuni investimenti

    with open("Profilazione.json") as json_file:

        data_lettura = json.load(json_file)


    return data_lettura




    