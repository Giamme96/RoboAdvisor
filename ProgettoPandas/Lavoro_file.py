
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

        try:                #Nel caso il json sia vuoto, quindiportafoglio vuoto
            data = json.load(json_file)  

            for i in data:
            
                GLOBE.AggiungiTitolo(data.get(i).get("isin"), data.get(i).get("nome"), data.get(i).get("symbol"), data.get(i).get("tipo_strumento"), data.get(i).get("country"), data.get(i).get("quantity"), data.get(i).get("position"), datetime.strptime(data.get(i).get("data_ordine"), '%Y-%m-%d %H:%M:%S.%f'), data.get(i).get("price_ordine"), -1)

        except JSONDecodeError:
        
            pass

def ScritturaQuestionarioSuFile():
    
    jsonfile = {}

        # "questionario" : questionario = {},
        # "checkbox" : checkbox = {}
    questionario = {}
    checkbox = {}
    
    for item in QUESTCTRL.QUESTIONARIOCTRL().lista_domande_questionario:
        
        index = 0

        temp_questionario = {
            
            "id" : index,
            "domanda" : item,
            "risposta" : QUESTCTRL.QUESTIONARIOCTRL().array_risposte_questionario[index]
        }

        jsonfile.get("questionario")[QUESTCTRL.QUESTIONARIOCTRL().lista_domande_questionario[index]] = temp_questionario

    for item in QUESTCTRL.QUESTIONARIOCTRL().lista_domande_questionario_checkbox():

        index = 0

        temp_checkbox = {

            "id" : index,
            "domanda" : item[0],
            "risposta" : item[QUESTCTRL.QUESTIONARIOCTRL().array_risposte_radio]
        }    
    
    jsonfile = {

        "questionario" : questionario,
        "checkbox" : checkbox
    }
       
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




    