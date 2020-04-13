import tkinter as tk
import matplotlib
import json
matplotlib.use('TkAgg')
import plotly.graph_objects as go
import pandas as pd


from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from pandas import DataFrame

import Plot_factory as PLOT   #Chiamata plotting
import API_call as CALLAPI
import globalita as GLOBE
import Tabella as TAB
import Metodi_calcolo as CALC



class QUESTIONARIOCTRL():

    questionario = 0

    lista_domande_questionario = ["Età",
                                    "Professione",
                                    "In quale tipologia di prodotti di tipo finanziario investe o ha investito in passato?",  
                                    "Quale è la sua fonte di reddito?",    
                                    "Quanto riesce a risparmiare del suo reddito annuo netto?", 
                                    "Quale percentuale investe dei suoi risparmi in prodotti finanziari?",
                                    "Quale è la sua reazione ai movimenti negativi di mercato?",
                                ]
    lista_domande_questionario_checkbox = [["Livello di istruzione", "1", "2", "3"],
                                            ["Lei è aggiornato sui mercati finanziari?", "1", "2", "3"],
                                            ["Con quale frequenza opera sul dossier titoli?", "1", "2", "3"],   
                                            ["Quale è la sua capacità reddituale annua netta?", "1", "2", "3"], 
                                            ["Quale è l'obiettivo dei suoi investimenti?", "1", "2", "3"],
                                            ["Quale è il periodi di tempo per il quale desidera conservare l'investimento?", "1", "2", "3"]
                                        ]

    def __init__(self, tabquestionario):

        self.questionario = tabquestionario

        self.frame_questionario = ttk.LabelFrame(self.questionario, text = "Compila il questionario con le domande aperte per la profilazione")
        self.frame_questionario.grid(column = 0, row = 0, sticky = "nswe")

        self.frame_radio = ttk.LabelFrame(self.questionario, text = "Compila il questionario con i radio buttons per la profilazione")
        self.frame_radio.grid(column = 0, row = 1, sticky = "nswe")

        self.invia_questionario = ttk.Button(self.questionario, text = "Invia")    #TODO da fare la callback e invio dati 
        self.invia_questionario.grid(column = 0, row = 2, sticky = "nswe")

        self.CreaQuestionario(self.frame_questionario)

        self.CreaRadio3Risposte(self.frame_radio)

    def CreaLabel(self, master, testo,  r, c):

        label = ttk.Label(master, text = testo)
        label.grid(column = c, row = r, sticky = "nswe")
    
    def CreaEntryWidget(self, master, r, c):      

        stringa = tk.StringVar()    #TODO da controllare 
        insert_data = tk.Entry(master)
        insert_data.grid(column = c, row = r)    
        
    def CreaRadio(self, master, domanda_corrente, r):   #crea tutti i radio nella lista passata [[domanda, 1, 2, 3]....]

        risposta = tk.StringVar() 
      
        index_risposte = 1
        first = True
        for i in domanda_corrente:

            if first:   #skip primo elemento
                
                first = False
                continue 
            
            radio = tk.Radiobutton(master, text = i, variable = risposta, value = index_risposte)
            radio.select()                          #TODO da controllare che serva a qualcosa
            radio.grid(column = index_risposte, row = r, sticky = "nswe")
            
            index_risposte += 1

    def CreaQuestionario(self, frame_master):    #Crea un questinario a domande aperte da una lista passata

        index = 0
        for i in self.lista_domande_questionario: #creazione domande aperte con entry
            
            self.CreaLabel(frame_master, i,  index, 0)
            self.CreaEntryWidget(frame_master, index, 1)

            index += 1

    def CreaRadio3Risposte(self, frame_master):     #Crea un questionario radio da una lista passata

        index = 0
        for i in self.lista_domande_questionario_checkbox:
            
            self.CreaLabel(frame_master, i[0], index, 0)
            self.CreaRadio(frame_master, i, index)

            index += 1


