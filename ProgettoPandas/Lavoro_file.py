
import json
from datetime import datetime

import globalita as GLOBE
import API_call as CALLAPI

def ScritturaPortafoglioSuFile():

    jsonfile = {}
    for i in GLOBE.titolo:

        temp = {
            "isin" : GLOBE.titolo.get(i).get("isin"),
            "nome" : GLOBE.titolo.get(i).get("nome"),
            "symbol" : GLOBE.titolo.get(i).get("symbol"),
            "tipo_strumento" : GLOBE.titolo.get(i).get("tipo_strumento"),
            "country" : GLOBE.titolo.get(i).get("country"),
            "quantity" : GLOBE.titolo.get(i).get("quantity"),
            "position" : GLOBE.titolo.get(i).get("position"),
            "data_ordine" : datetime.strftime(GLOBE.titolo.get(i).get("data_ordine"), '%Y-%m-%d %H:%M:%S.%f'),
            "price_ordine" : GLOBE.titolo.get(i).get("price_ordine"),
            "totale_ordine" : GLOBE.titolo.get(i).get("totale_ordine"),
            "change_dall_acquisto" : GLOBE.titolo.get(i).get("totale_change"),
            "currency" : GLOBE.titolo.get(i).get("currency")
        }

        jsonfile[GLOBE.titolo.get(i).get("isin")] = temp
    
    with open("Portafoglio.json", "w") as outfile:

        json.dump(jsonfile, outfile)

def LetturaPortafoglioDaFile():

    with open('Portafoglio.json') as json_file:

        data = json.load(json_file)
                
        for i in data:
        
            GLOBE.AggiungiTitolo(data.get(i).get("isin"), data.get(i).get("nome"), data.get(i).get("symbol"), data.get(i).get("tipo_strumento"), data.get(i).get("country"), data.get(i).get("quantity"), data.get(i).get("position"), datetime.strptime(data.get(i).get("data_ordine"), '%Y-%m-%d %H:%M:%S.%f'), data.get(i).get("price_ordine"), -1)

def ScritturaSuProfilazione():    #la posizione dell'utente investitore

    json_profilazione = {

        "classificazione_rischio" : "speculazione"  #speculazione, risparmio, crescita capitale

    }

    with open("Profilazione.json", "w") as outfile:

        json.dump(json_profilazione, outfile)

def LetturaDaProfilazione():  #da utilizzare la profilazione dell'investitore per permettere alcuni investimenti

    with open("Profilazione.json") as json_file:

        data_lettura = json.load(json_file)


    return data_lettura




    