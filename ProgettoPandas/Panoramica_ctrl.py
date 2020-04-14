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
    def __init__(self, tabpanoramica):
        
        self.panoramica = tabpanoramica

        #Creazione labelframe modulo display portafoglio ---------------------------------------------------------------------------------PORTAFOGLIO
        self.frame_port = ttk.LabelFrame(self.panoramica, text = 'Portafoglio titoli')
        self.frame_port.grid(column = 0, row = 0, sticky = "nswe")


        #TODO controllo su elementi societa
        
        TAB.Tabella(self.frame_port)
        

        frame_portafoglio = ttk.LabelFrame(self.panoramica, text = "Overview portafoglio")
        frame_portafoglio.grid(column = 0, row = 1, sticky = "nswe")

        label_totale_investimento = ttk.Label(frame_portafoglio, text = f"Il totale investito è: {CALC.TotaleInvestimento()}")
        label_totale_investimento.grid(column = 0, row = 0, sticky = "nswe")


        label_rendimento = ttk.Label(frame_portafoglio, text = f"Il rendimento atteso di portafoglio è: {CALC.RendimentoAttesoPortafoglio()}")
        label_rendimento.grid(column = 0, row = 1, sticky = "nsw")

        label_rischio = ttk.Label(frame_portafoglio, text = f"Il rischio di portafoglio è: {CALC.CalcolaDevStdPortafoglio()}")
        label_rischio.grid(column = 0, row = 2, sticky = "nswe")

        label_beta = ttk.Label(frame_portafoglio, text = f"Il beta di portafoglio è: {CALC.BetaPortafoglio()}")
        label_beta.grid(column = 0, row = 3, sticky = "nswe")

