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

class PANORAMICACTRL():

    #Reference tab panoramica
    panoramica = 0
    frame_port = 0

    tot_investimento = 0
    rendimento_atteso = 0
    dev_std = 0
    beta_portafoglio = 0


    testo_tot_investimento = "Il totale investito è: "
    testo_rendimento = "Il rendimento atteso di portafoglio è: "
    testo_rischio = "Il rischio di portafoglio è: "
    testo_beta = "Il beta di portafoglio è: "
    def __init__(self, tabpanoramica):
        
        self.panoramica = tabpanoramica

        
        self.tot_investimento = tk.StringVar()
        self.rendimento_atteso = tk.StringVar()
        self.dev_std = tk.StringVar()
        self.beta_portafoglio = tk.StringVar()

        #Creazione labelframe modulo display portafoglio ---------------------------------------------------------------------------------PORTAFOGLIO
        self.frame_port = ttk.LabelFrame(self.panoramica, text = 'Portafoglio titoli')
        self.frame_port.grid(column = 0, row = 0, sticky = "nswe")

        TAB.Tabella(self.frame_port)
        self.SetPanoramicaTechValues()

        frame_portafoglio = ttk.LabelFrame(self.panoramica, text = "Overview portafoglio")
        frame_portafoglio.grid(column = 0, row = 1, sticky = "nswe")

        label_totale_investimento = ttk.Label(frame_portafoglio, textvariable =self.tot_investimento)
        label_totale_investimento.grid(column = 0, row = 0, sticky = "nswe")

        label_rendimento = ttk.Label(frame_portafoglio, textvariable = self.rendimento_atteso)
        label_rendimento.grid(column = 0, row = 1, sticky = "nsw")

        label_rischio = ttk.Label(frame_portafoglio, textvariable = self.dev_std)
        label_rischio.grid(column = 0, row = 2, sticky = "nswe")

        label_beta = ttk.Label(frame_portafoglio, textvariable = self.beta_portafoglio)
        label_beta.grid(column = 0, row = 3, sticky = "nswe")

        
    def SetPanoramicaTechValues(self):

        self.tot_investimento.set(self.testo_tot_investimento + str(round(CALC.TotaleInvestimento(), 2)))
        self.rendimento_atteso.set(self.testo_rendimento + str(round(CALC.RendimentoAttesoPortafoglio(), 2)))
        self.dev_std.set(self.testo_rischio + str(round(CALC.CalcolaDevStdPortafoglio(), 2)))
        self.beta_portafoglio.set(self.testo_beta + str(round(CALC.BetaPortafoglio(), 2)))
