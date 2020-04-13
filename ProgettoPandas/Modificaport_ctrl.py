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
from pandas import DataFrame
from tkinter import messagebox as msg

import globalita as GLOBE
import InterpreterAPI as INTPR
import API_call as CALLAPI
import Plot_factory as PLOT
import Metodi_calcolo as CALC
import Lavoro_file as FILE

class MODIFICAPORTCTRL():

    #Reference TAB
    modificaport = 0

    #reference a frame CERCA
    societacerca = 0
    lblrend = 0
    lblstd = 0

    testolabelrend = "Il rendimento medio del titolo è: "
    testolabelstd = "La dev. std è: "
    valuelabelrend = ""
    valuelabelstd = ""

    periodo_sel = 0
    data_sel = 0

    #reference a frame AGGIUNGI
    quantity_agg = 0    #input quantità
    position_agg = 0    #input posizione    0 = long 1 = short
    societa = 0     #input societa
    
    #reference a frame MODIFICA
    societa_modifica = 0
    position_modifica = 0
    quantity_modifica = 0
    combosocieta_modifica = 0
    
    

    def __init__(self, tabmodificaport):
        
        self.modificaport = tabmodificaport

        #Creazione labelframe modulo cerca ---------------------------------------------------------------------------------CERCA
        frame_cerca = ttk.LabelFrame(self.modificaport, text = 'Overview titolo')
        frame_cerca.grid(column = 0, row = 0, sticky = "w")
        

        #Creazione menu a tendina elenco società
        self.societa_cerca = tk.StringVar()
        combosocieta_cerca = ttk.Combobox(frame_cerca, state = 'readonly', textvariable = self.societa_cerca)
        combosocieta_cerca['values'] = list(GLOBE.lista_NASDAQ.keys())
        combosocieta_cerca.grid(column = 0, row = 0, sticky = "w")
        combosocieta_cerca.current(0)

        #Creazione menu a tendina elenco periodizzazione dati   DA GUARDARE
        self.periodo_sel = tk.StringVar()
        periodi = ['Daily', 'Weekly', 'Monthly']
        combodata = ttk.Combobox(frame_cerca, state = 'readonly', values = periodi , textvariable = self.periodo_sel)
        combodata.grid(column = 1, row = 0)
        combodata.current(0)        

        #creazione entry widget per l'inserimento della data
        self.data_sel = tk.StringVar()
        self.insert_data = tk.Entry(frame_cerca)
        self.insert_data.grid(column = 2, row = 0)
        
        #adding a button CERCA
        query_cerca = ttk.Button(frame_cerca, text = "Cerca", command = self.CallBackCerca)     
        query_cerca.grid(column = 3, row = 0)

        #display rendimento e std aggiornato ogni callbackcerca
        self.valuelabelrend = tk.StringVar()
        self.valuelabelrend.set(self.testolabelrend + "0")
        self.lblrend = ttk.Label(frame_cerca, textvariable = self.valuelabelrend)
        self.lblrend.grid(column = 0, row = 2)

        self.valuelabelstd = tk.StringVar()
        self.valuelabelstd.set(self.testolabelstd + "0")
        self.lblstd = ttk.Label(frame_cerca, textvariable = self.valuelabelstd)
        self.lblstd.grid(column = 0, row = 3)

        #Creazione labelframe modulo cerca ---------------------------------------------------------------------------------CERCA^^^

        #Creazione labelframe modulo aggiungi ******************************************************************************AGGIUNGI
     
        frame_aggiungi = ttk.LabelFrame(self.modificaport, text = 'Aggiungi titolo')
        frame_aggiungi.grid(column = 0, row = 1, sticky = "W")

        #Creazione menu a tendina titoli
       
        self.societa = tk.StringVar()
        combosocieta = ttk.Combobox(frame_aggiungi, state = 'readonly', textvariable = self.societa)
        combosocieta['values'] = list(GLOBE.lista_NASDAQ.keys())
        combosocieta.grid(column = 0, row = 0)
        combosocieta.current(0)

        #adding a Textbox entry per le quantità
        self.quantity_agg = tk.IntVar() # il totale dovrà essere minore del cash disponibile *da vedere*

        insertqt_agg = ttk.Entry(frame_aggiungi, textvariable = self.quantity_agg) # la quantità deve essere un intero e non inferiore a 0
        insertqt_agg.grid(column = 1, row = 0)

        #Creating radio buttons (SHORT-LONG)
        self.position_agg = tk.IntVar()

        check_longagg = tk.Radiobutton(frame_aggiungi, text = "Long", variable = self.position_agg, value = 0)     #0 = LONG
        check_longagg.select()
        check_longagg.grid(column = 0, row = 1, sticky = tk.W)
 
        check_shortagg = tk.Radiobutton(frame_aggiungi, text = "Short", variable = self.position_agg, value = 1)    #1 = SHORT
        check_shortagg.deselect()
        check_shortagg.grid(column = 1, row = 1, sticky = tk.W)
           
        #adding a button
        query_aggiungi = ttk.Button(frame_aggiungi, text = "Inserisci", command = self.CallBackInserisci)
        query_aggiungi.grid(column = 3, row = 0)

        #Creazione labelframe modulo aggiungi ******************************************************************************AGGIUNGI^^^

        #Creazione labelframe modulo modifica ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MODIFICA

        frame_modifica = ttk.LabelFrame(self.modificaport, text = "Modifica portafoglio")
        frame_modifica.grid(column = 0, row = 2, sticky = "W")

        #creazione menu a tendina società
        self.societa_modifica = tk.StringVar()
        self.combosocieta_modifica = ttk.Combobox(frame_modifica, state = 'readonly', textvariable = self.societa_modifica)
        self.combosocieta_modifica['values'] = GLOBE.CheckListaModPortafoglio()
        self.combosocieta_modifica.grid(column = 0, row = 0)
        # combosocieta_modifica.current()

        #Creating radio buttons (SHORT-LONG)
        self.position_modifica = tk.IntVar()

        check_longmod = tk.Radiobutton(frame_modifica, text = "Long", variable = self.position_modifica, value = 0)     #0 = LONG
        check_longmod.select()
        check_longmod.grid(column = 0, row = 1, sticky = tk.W)
 
        check_shortmod = tk.Radiobutton(frame_modifica, text = "Short", variable = self.position_modifica, value = 1)    #1 = SHORT
        check_shortmod.deselect()
        check_shortmod.grid(column = 1, row = 1, sticky = tk.W)

        #adding a Textbox entry per le quantità
        self.quantity_modifica = tk.IntVar() # il totale dovrà essere minore del cash disponibile *da vedere*
        insertqt_mod = ttk.Entry(frame_modifica, textvariable = self.quantity_modifica) # la quantità deve essere un intero e non inferiore a 0
        insertqt_mod.grid(column = 1, row = 0)

        #adding a button
        query_modifica = ttk.Button(frame_modifica, text = "Modifica", command = self.CallbackModifica)
        query_modifica.grid(column = 3, row = 0)
         #Creazione labelframe modulo modifica ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MODIFICA^^^    

    def CallBackInserisci(self):
        
        print("Callbackinserisci .......")
        print(self.quantity_agg.get())
        print(GLOBE.lista_NASDAQ.get(self.societa.get()))
        print(self.position_agg.get())

        symbol = GLOBE.lista_NASDAQ.get(self.societa.get())     #restituisce il simbolo associato al nome inviato a Lista_NASDQ

        if GLOBE.societa.get(symbol) == None or GLOBE.societa.get("quantity") == 0:
            
            if self.quantity_agg.get() > 0:     #controllo quantità inserita maggiore di 0

                dfp = CALLAPI.BEESCALLER().AdjApiCallPortafoglio(symbol) 
                GLOBE.AggiungiSocieta(self.societa.get(), self.quantity_agg.get(), self.position_agg.get(), datetime.now(), dfp["Close"].iloc[len(dfp) - 1], dfp)
                self.combosocieta_modifica['values'] = GLOBE.CheckListaModPortafoglio()

                FILE.ScritturaPortFile()
                    
    def CallbackModifica(self):            

        print("Callbackmodifica .......")
        print(self.quantity_modifica.get())
        print(GLOBE.lista_NASDAQ.get(self.societa_modifica.get()))
        print(self.position_modifica.get())

        symbol = GLOBE.lista_NASDAQ.get(self.societa_modifica.get())     #restituisce il simbolo associato al nome inviato a Lista_NASDQ

        quantita = self.quantity_modifica.get()

        position = self.position_modifica.get()

        if quantita == 0:       #se la quantità inserita in modifica è 0, si tramuta in un'eliminaizone dal portafoglio
   
           del GLOBE.societa[symbol]
           self.combosocieta_modifica['values'] = GLOBE.CheckListaModPortafoglio()
           self.combosocieta_modifica.current(0)
        elif quantita >= GLOBE.societa.get(symbol)["quantity"]:

            msg.showerror("Errore", "Sono ammesse solo operazioni di vendita")
            return 
        else:

            GLOBE.societa.get(symbol)["quantity"] = quantita
            GLOBE.societa.get(symbol)["position"] = position
            

        FILE.ScritturaPortFile()

    def CallBackCerca(self):

        print("CallbackCerca.....", GLOBE.lista_NASDAQ.get(self.societa_cerca.get()))
        
        periodo_dati = self.periodo_sel.get()

        data_dati = self.insert_data.get()

        symbol = GLOBE.lista_NASDAQ.get(self.societa_cerca.get())    #restituisce il simbolo associato al nome inviato a Lista_NASDQ


        df = CALLAPI.BEESCALLER().AdjApiCall(symbol, periodo_dati, data_dati)      

        self.valuelabelrend.set(self.testolabelrend + str(CALC.DeltaChangeAvg(df, 'Close')))
        self.valuelabelstd.set(self.testolabelstd + str(CALC.DeltaChangeStd(df, 'Close')))
        
        PLOT.PLOTFACTORY().SubPlotLineeBarre(symbol, df, 'Close', 10, 5, 5)

