from datetime import datetime
import json
import tkinter as tk
import Metodi_calcolo as CALC
import API_call as CALLAPI
import Lavoro_file as FILE

titolo = {}    
questionario = {}
radio = {}

profilazione = False

country_isin = {            #da completare con tutti i riferimenti
        "US" : "united states",
        "IT" : "italy",
        "GB" : "great britain"
    }

mappa_strumenti = {

        "stock" : "stock",
        "etf" : "etf",
        "fund" : "fund"
    }

mappa_periodicita = {

        "Daily" : "Daily",
        "Weekly" : "Weekly",
        "Monthly" : "Monthly"
    }


    
def AggiungiTitolo(isin, nome, symbol, tipologia_strumento, country, quantita, date, price, dataframe_dict):

    Titolo_dict = {

        "isin" : isin,
        "nome": nome,
        "symbol" : symbol,
        "tipo_strumento" : tipologia_strumento,
        "country" : country,
        "data_ordine" : date,
        "beta" : CALC.GetItemFromInfoTech(dataframe_dict, tipologia_strumento, "Beta"), 
        "price_ordine" : price,
        "quantity" : quantita,
        "totale_ordine" : CALC.RoundCalcolo(price * quantita, True),
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

def DatiQuestionario(lista_domande_questionario, array_risposte_questionario):

    global questionario

    index = 0

    for item in lista_domande_questionario:
        
        temp_questionario = {
            
            "id" : index,
            "domanda" : item,
            "risposta" : array_risposte_questionario[index].get()
        }

        questionario[index] = temp_questionario    

        index += 1

def DatiRadio(lista_domande_questionario_radio, array_risposte_radio):

    global radio

    index = 0

    for item in lista_domande_questionario_radio:

        temp_radio = {

            "id" : index,
            "domanda" : item[0],
            "risposta" : item[array_risposte_radio[index].get()]
        }    

        radio[index] = temp_radio
        index += 1



