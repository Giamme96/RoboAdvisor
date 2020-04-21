import tkinter as tk
import matplotlib
import json
matplotlib.use('TkAgg')
import plotly.graph_objects as go
import pandas as pd
import statistics as stat

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from pandas import DataFrame
from tkinter import messagebox as msg

import Plot_factory as PLOT   #Chiamata plotting
import API_call as CALLAPI
import globalita as GLOBE
import Tabella as TAB
import Metodi_calcolo as CALC
import Lavoro_file as FILE
import View_manager as MANAGER


class QUESTIONARIOCTRL():

    questionario = 0

    array_risposte_questionario = []
    array_risposte_radio = []
    

    lista_domande_questionario = ["Età",
                                    "Professione",
                                    "In quale tipologia di prodotti di tipo finanziario investe o ha investito in passato?",  
                                    "Quale è la sua fonte di reddito?",    
                                    "Quanto riesce a risparmiare del suo reddito annuo netto?", 
                                    "Quale percentuale investe dei suoi risparmi in prodotti finanziari?",
                                ]
    lista_domande_questionario_radio = [["Livello di istruzione", "Elementare", "Superiore", "Università"],
                                            ["Lei è aggiornato sui mercati finanziari?", "No", "Si"],  
                                            ["Come reagisce ai movimenti negativi di mercato?", "Panic selling", "Agisco razionalmente"], 
                                            ["Quale è l'obiettivo dei suoi investimenti?", "Speculazione", "Crescita capitale", "Risparmio"],
                                            ["Quale è il periodo di tempo per il quale desidera conservare l'investimento?", "< 12 mesi", "tra 1 e 5 anni", "> 5 anni"],
                                            ["Se potesse scegliere uno solo tra due pacchi occultati, contenenti 0 euro e 1 euro, e le venissero offerti 50 cent, cosa farebbe?", "Scelgo un pacco", "Accetto l'offerta"]
                                        ]

    def __init__(self, tabquestionario):

        self.questionario = tabquestionario

        self.frame_questionario = ttk.LabelFrame(self.questionario, text = "Compila il questionario con le domande aperte per la profilazione")
        self.frame_questionario.grid(column = 0, row = 0, sticky = "nswe")

        self.frame_radio = ttk.LabelFrame(self.questionario, text = "Compila il questionario con i radio buttons per la profilazione")
        self.frame_radio.grid(column = 0, row = 1, sticky = "nswe")

        self.invia_questionario = ttk.Button(self.questionario, text = "Invia", command = self.CallBackQuestionario)    #TODO da fare la callback e invio dati 
        self.invia_questionario.grid(column = 0, row = 2, sticky = "nswe")

        self.CreaQuestionario(self.frame_questionario)

        self.CreaRadio3Risposte(self.frame_radio)
        
    def CreaLabel(self, master, testo,  r, c):
        
        label = ttk.Label(master, text = testo)
        label.grid(column = c, row = r, sticky = "nswe")
    
    def CreaEntryWidget(self, master, r, c):      

        stringa = tk.StringVar()    #TODO da controllare 
        insert_data = tk.Entry(master, textvariable = stringa)
        insert_data.grid(column = c, row = r)
        self.array_risposte_questionario.append(stringa)    
        
    def CreaRadio(self, master, domanda_corrente, r):   #crea tutti i radio nella lista passata [[domanda, 1, 2, 3]....]

        risposta = tk.IntVar() 
             
        index_risposte = 1
        first = True
        for i in domanda_corrente:

            if first:   #skip primo elemento
                
                first = False
                continue 
           
            radio = tk.Radiobutton(master, text = i, variable = risposta, value = index_risposte)
            radio.deselect()                         
            radio.grid(column = index_risposte, row = r, sticky = "nswe")
            
            index_risposte += 1

        self.array_risposte_radio.append(risposta)

    def CreaQuestionario(self, frame_master):    #Crea un questinario a domande aperte da una lista passata

        index = 0
        for i in self.lista_domande_questionario: #creazione domande aperte con entry
            
            self.CreaLabel(frame_master, i,  index, 0)
            self.CreaEntryWidget(frame_master, index, 1)

            index += 1

    def CreaRadio3Risposte(self, frame_master):     #Crea un questionario radio da una lista passata

        index = 0
        for i in self.lista_domande_questionario_radio:
            
            self.CreaLabel(frame_master, i[0], index, 0)
            self.CreaRadio(frame_master, i, index)

            index += 1
    
    def CallBackQuestionario(self):

        risposte_questionario = self.array_risposte_questionario
        risposte_radio = self.array_risposte_radio

        if len(risposte_radio) != len(self.lista_domande_questionario_radio) and len(risposte_questionario) != len(self.lista_domande_questionario): #controllo risposte a tutte le domande
            
            msg.showwarning(title = "Problema inserimento", message = "Controlla di aver risposto a tutte le domande!")

            return

        GLOBE.DatiQuestionario(self.lista_domande_questionario, risposte_questionario)
        GLOBE.DatiRadio(self.lista_domande_questionario_radio, risposte_radio)
        FILE.ScritturaQuestionarioSuFile()  #scrittura su file questionario
        FILE.ScritturaRadioSuFile()

        punteggio = [] 
        numero_risposte_per_domanda = []  #numero risposte per ogni domanda

        soglia_bassa = 0.5
        soglia_media = 0.75
        # soglia_alta = 1
        
        index = 0

        for i in self.lista_domande_questionario_radio:
            
            numero_risposte_per_domanda.append(len(i) - 1)

        if len(risposte_radio) == len(numero_risposte_per_domanda):

            for i in risposte_radio:

                quoziente = i.get() / numero_risposte_per_domanda[index]      #.get

                punteggio.append(quoziente)

                index += 1

            media_punteggio = stat.mean(punteggio)      #viene assegnato un punteggio al questionario dell'utente per determinare la categoria

            if media_punteggio <= soglia_bassa:

                FILE.ScritturaSuProfilazione("Livello Basso")

            elif media_punteggio >= soglia_media:

                FILE.ScritturaSuProfilazione("Livello Alto")

            else:

                FILE.ScritturaSuProfilazione("Livello Medio")
            
            msg.showinfo(title = "Operazione eseguita", message = "Invio effettuato con successo!")




        
