
import json
from datetime import datetime
from json.decoder import JSONDecodeError

import globalita as GLOBE
import API_call as CALLAPI
import Questionario_ctrl as QUESTCTRL


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

        try:                #Nel caso il json sia vuoto, quindiportafoglio vuoto
            data = json.load(json_file)  

            for i in data:
            
                GLOBE.AggiungiTitolo(data.get(i).get("isin"), data.get(i).get("nome"), data.get(i).get("symbol"), data.get(i).get("tipo_strumento"), data.get(i).get("country"), data.get(i).get("quantity"), datetime.strptime(data.get(i).get("data_ordine"), '%Y-%m-%d %H:%M:%S.%f'), data.get(i).get("price_ordine"), -1)

        except JSONDecodeError:
        
            pass

def ScritturaQuestionarioSuFile():  #scrive su file un nested dict con domande e risposte ricevute dal questionario

    jsonfile = {}
    
    
    for item in GLOBE.questionario:
      
        temp_questionario = {
            
            "id" : item,
            "domanda" : GLOBE.questionario.get(item).get("domanda"),
            "risposta" : GLOBE.questionario.get(item).get("risposta")
        }

        jsonfile[item] = temp_questionario


    with open("Questionario.json", "w") as outfile:

        json.dump(jsonfile, outfile)

def ScritturaRadioSuFile():

    jsonfile = {}

    for item in GLOBE.radio:

        temp_radio = {

            "id" : item,
            "domanda" : GLOBE.radio.get(item).get("domanda"),
            "risposta" : GLOBE.radio.get(item).get("risposta")
        }    

        jsonfile[item] = temp_radio

    with open("Radio.json", "w") as outfile:

       json.dump(jsonfile, outfile)

def LetturaQuestionarioDaFile():

    with open("Questionario.json") as json_file:

        data = json.load(json_file)

        for i in data:
            
            GLOBE.questionario[i] = {
                "id" : data.get(i).get("id"),
                "domanda" : data.get(i).get("domanda"),
                "risposta" : data.get(i).get("risposta")
            }
        

def LetturaRadioDaFile():

    with open("Radio.json") as json_file:

        data = json.load(json_file)

        for i in data:
            
            GLOBE.radio[i] = {
                "id" : data.get(i).get("id"),
                "domanda" : data.get(i).get("domanda"),
                "risposta" : data.get(i).get("risposta")
            }

def ScritturaSuProfilazione(categoria_utente):    #la posizione dell'utente investitore

    json_profilazione = {

        "classificazione_rischio" : categoria_utente  
    }

    with open("Profilazione.json", "w") as outfile:

        json.dump(json_profilazione, outfile)

def LetturaDaProfilazione():  #da utilizzare la profilazione dell'investitore per permettere alcuni investimenti

    with open("Profilazione.json") as json_file:
    
        try:
            profilazione_data = json.load(json_file)

            GLOBE.profilazione = profilazione_data
        
        except JSONDecodeError:

            pass
       




    