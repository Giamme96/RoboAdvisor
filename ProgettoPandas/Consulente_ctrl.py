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

class CONSULENTECTRL():

    consulente = 0

    testo_beta_1 = "Il beta del tuo portafoglio è : "
    testo_beta_2 = ", considera che questo agisce come moltiplicatore dei movimenti di mercato. \n"
    testo_esposizione = "Un portafoglio ben strutturato non deve avere esposizioni troppo elevate ad un singolo titolo. \nDovresti ridurre l'esposizione verso questi titoli, modificando le quantità o aumentando l'investimento totale: "
    testo_diversificazione = "Un portafoglio ben diversificato permette una grossa riduzione del rischio. \n"

    value_beta = 0
    value_esposizione = 0
    value_diversificazione = 0




    def __init__(self, tabconsulente):

        self.consulente = tabconsulente

        self.value_beta = tk.StringVar()
        self.value_esposizione = tk.StringVar()
        self.value_diversificazione = tk.StringVar()

        self.SetConsulenteValues()

        labelframe_beta = ttk.LabelFrame(self.consulente, text = "BETA PORTAFOGLIO")
        labelframe_beta.grid(column = 0, row = 0, sticky = "nswe")
        label_beta = ttk.Label(labelframe_beta, textvariable = self.value_beta)
        label_beta.grid(column = 0, row = 0, sticky = "nswe")

        labelframe_diversificazione = ttk.LabelFrame(self.consulente, text = "DIVERSIFICAZIONE PORTAFOGLIO")
        labelframe_diversificazione.grid(column = 0, row = 1, sticky = "nswe", pady = 20)
        label_diversificazione = ttk.Label(labelframe_diversificazione, textvariable = self.value_diversificazione)
        label_diversificazione.grid(column = 0, row = 0, sticky = "nswe")

        labelframe_esposizione = ttk.LabelFrame(self.consulente, text = "ESPOSIZIONE TITOLI")
        labelframe_esposizione.grid(column = 0, row = 2, sticky = "nswe")
        label_esposizione = ttk.Label(labelframe_esposizione, textvariable = self.value_esposizione)
        label_esposizione.grid(column = 0, row = 0, sticky = "nswe")

    def SetConsulenteValues(self):

        self.value_beta.set(self.testo_beta_1 + str(round(CALC.BetaPortafoglio(), 2)) + self.testo_beta_2 + str(self.ConsiglioBeta()))
        self.value_diversificazione.set(self.testo_diversificazione + str(self.ConsiglioDiversificazione()))
        self.value_esposizione.set(self.testo_esposizione + str(self.ConsiglioEsposizione()))


    def ConsiglioDiversificazione(self):

        if not GLOBE.titolo:
            
            return 

        soglia_titoli = 20

        if len(GLOBE.titolo) <= soglia_titoli:

            consiglio = "Ti consiglio vivamente di aumentare i titoli nel tuo portafoglio per una migliore diversificazione."
        
        return consiglio
    
    def ConsiglioBeta(self):
        
        if not GLOBE.titolo:

            return 
        
        if not GLOBE.radio:

            return
        
        if GLOBE.radio != None:
       
            if GLOBE.radio["3"].get("risposta"):

                consiglio = "Ti consiglio di inserire titoli con un rischio non troppo elevato."
            
                return consiglio

            elif GLOBE.radio["3"].get("risposta") == "Speculazione":

                consiglio = "Ti consiglio di inserire anche titoli con un Beta alto, per aumentare le possibilità di alti profitti."

                return consiglio        
    
    def ConsiglioEsposizione(self):

        if not GLOBE.titolo:
            
            return
                    
        soglia = 0.20
        titoli_over = []
        totale = CALC.TotaleInvestimento()
        for i in GLOBE.titolo.values():

            if (i.get("totale_ordine") / totale) >= soglia:

                titoli_over.append(i.get("symbol"))
        
        return titoli_over


              
      



                

