import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Plot_factory as PLOT   #Chiamata plotting
import json
from datetime import datetime

import globalita as GLOBE
import InterpreterAPI as INTPR
import API_call as CALLAPI
import Plot_factory as PLOT
import Metodi_calcolo as CALC

class MODIFICAPORTCTRL():

    #Reference tab modificaport
    modificaport = 0
    quantity = 0    #input quantità
    position = 0    #input posizione    0 = long 1 = short
    societa = 0     #input societa
    societacerca = 0

    lblframe_botL = 0
    lblframe_botR = 0
    
    lblrend = 0
    lblstd = 0

    testolabelrend = "Il rendimento medio del titolo è: "
    testolabelstd = "La dev. std è: "

    valuelabelrend = ""
    valuelabelstd = ""

    periodo_sel = 0

    data_sel = 0

    def __init__(self, tabmodificaport):
        
        self.modificaport = tabmodificaport

        #Creazione labelframe modulo cerca ---------------------------------------------------------------------------------CERCA
        labeldesc1 = ttk.LabelFrame(self.modificaport, text = 'Overview titolo')
        labeldesc1.grid(column = 0, row = 0)

        #Creazione menu a tendina elenco società
        self.societacerca = tk.StringVar()
        combosocietacerca = ttk.Combobox(labeldesc1, state = 'readonly', textvariable = self.societacerca)
        combosocietacerca['values'] = list(GLOBE.lista_NASDAQ.keys())
        combosocietacerca.grid(column = 0, row = 0)
        combosocietacerca.current(0)

        #Creazione menu a tendina elenco periodizzazione dati   DA GUARDARE
        self.periodo_sel = tk.StringVar()
        periodi = ['daily', 'weekly', 'monthly']
        combodata = ttk.Combobox(labeldesc1, state = 'readonly', values = periodi , textvariable = self.periodo_sel)
        combodata.grid(column = 1, row = 0)
        print()
        combodata.current(0)

        #creazione entry widget per l'inserimento della data
        self.data_sel = tk.StringVar()
        self.insert_data = tk.Entry(labeldesc1)
        self.insert_data.grid(column = 1, row = 1)

        
        #adding a button CERCA
        query_api = ttk.Button(labeldesc1, text = "Cerca", command = self.CallBackCerca)        #da cambiare la funzione
        query_api.grid(column = 2, row = 0)

        #display rendimento e std aggiornato ogni callbackcerca
        self.valuelabelrend = tk.StringVar()
        self.valuelabelrend.set(self.testolabelrend + "0")
        self.lblrend = ttk.Label(labeldesc1, textvariable = self.valuelabelrend)
        self.lblrend.grid(column = 0, row = 2)

        self.valuelabelstd = tk.StringVar()
        self.valuelabelstd.set(self.testolabelstd + "0")
        self.lblstd = ttk.Label(labeldesc1, textvariable = self.valuelabelstd)
        self.lblstd.grid(column = 0, row = 3)
        #Creazione labelframe modulo cerca ---------------------------------------------------------------------------------CERCA

        #Creazione labelframe modulo aggiungi ******************************************************************************AGGIUNGI
     
        labeldesc2 = ttk.LabelFrame(self.modificaport, text = 'Aggiungi titolo')
        labeldesc2.grid(column = 3, row = 0, sticky = "N")
  
        #Creazione menu a tendina e button        
       
        self.societa = tk.StringVar()
        combosocieta = ttk.Combobox(labeldesc2, state = 'readonly', textvariable = self.societa)
        combosocieta['values'] = list(GLOBE.lista_NASDAQ.keys())
        combosocieta.grid(column = 3, row = 0)
        combosocieta.current(0)

        #adding a Textbox entry per le quantità
        self.quantity = tk.IntVar() # il totale dovrà essere minore del cash disponibile *da vedere*

        insertqt = ttk.Entry(labeldesc2, textvariable = self.quantity) # la quantità deve essere un intero e non inferiore a 0
        insertqt.grid(column = 4, row = 0)
        
        #Creating radio buttons (SHORT-LONG)
        self.position = tk.IntVar()

        check1 = tk.Radiobutton(labeldesc2, text = "Long", variable = self.position, value = 0)     #0 = LONG
        check1.select()
        check1.grid(column = 3, row = 1, sticky = tk.W)

        check2 = tk.Radiobutton(labeldesc2, text = "Short", variable = self.position, value = 1)    #1 = SHORT
        check2.deselect()
        check2.grid(column = 4, row = 1, sticky = tk.W)
           
        #adding a button
        query_api = ttk.Button(labeldesc2, text = "Inserisci", command = self.CallBackInserisci)
        query_api.grid(column = 5, row = 0)
        #Creazione labelframe modulo aggiungi ******************************************************************************AGGIUNGI


        # #creazione label frame bot sinistra
        # self.lblframe_botL = ttk.Frame(self.modificaport)
        # self.lblframe_botL.grid(column = 1, row = 3, padx = 10)

        # #Creazione label frame bot destra
        # self.lblframe_botR = ttk.Frame(self.modificaport)
        # self.lblframe_botR.grid(column = 4, row = 3, padx = 10)

        

    def CallBackInserisci(self):
        
        print("Callbackinserisci .......")
        print(self.quantity.get())
        print(GLOBE.lista_NASDAQ.get(self.societa.get()))
        print(self.position.get())

        symbol = GLOBE.lista_NASDAQ.get(self.societa.get())

        if GLOBE.societa.get(symbol) == None:

            GLOBE.AggiungiSocieta(self.societa.get(), self.quantity.get(), self.position.get(), datetime.now())
        
    def CallBackCerca(self):

        print("CallbackCerca.....", GLOBE.lista_NASDAQ.get(self.societacerca.get()))
        
        periodo_dati = self.periodo_sel.get()

        data_dati = self.insert_data.get()

        symbol = GLOBE.lista_NASDAQ.get(self.societacerca.get())

        df = CALLAPI.BEESCALLER().AdjApiCall(symbol, periodo_dati, data_dati)      

        self.valuelabelrend.set(self.testolabelrend + str(CALC.DeltaChangeAvg(df, 'Close')))
        self.valuelabelstd.set(self.testolabelstd + str(CALC.DeltaStd(df, 'Close')))
  
     
        # df1 = df.copy()
        # # #richiamo grafici
        # canvasleft = FigureCanvasTkAgg(PLOT.PLOTFACTORY().PlotLineePanda(symbol, df, 'adjusted close', 25, 3, 2), master = self.lblframe_botL)
        # # canvasleft._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)  
        # canvasleft._tkcanvas.pack()

        # canvasright = FigureCanvasTkAgg(PLOT.PLOTFACTORY().PlotRendimentoPanda(symbol, df1, 'adjusted close', 3, 2), master = self.lblframe_botR)
        # # canvasright._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)  
        # canvasright._tkcanvas.pack()
        
        PLOT.PLOTFACTORY().SubPlotLineeBarre(symbol, df, 'Close', 10, 4, 4)
        
