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

    def __init__(self, tabconsulente):

        self.consulente = tabconsulente

        frame_consulente = ttk.LabelFrame(self.consulente, text = "Overview consulente, consigli utili...")
        frame_consulente.grid(column = 0, row = 0, sticky = "nswe")

        # label_beta = ttk.Label(frame_consulente, text = f"Il beta del tuo portafoglio è : {CALC.BetaPortafoglio}, considera che questo agisce come moltiplicatore dei movimenti di mercato. ")
        # label_totale_investimento.grid(column = 0, row = 0, sticky = "nswe")

    def ConsiglioDiversificazione(self):

        soglia_titoli = 20

        if len(GLOBE.titolo) <= soglia_titoli:

            consiglio = "Ti consiglio vivamente di aumentare i titoli nel tuo portafoglio per una migliore diversificazione."
        
        return consiglio

        

