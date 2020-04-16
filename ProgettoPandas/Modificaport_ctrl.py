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
import API_call as CALLAPI
import Plot_factory as PLOT
import Metodi_calcolo as CALC
import Lavoro_file as FILE

class MODIFICAPORTCTRL():

    #Reference TAB
    modificaport = 0

    #reference a frame CERCA
    titolo_cerca = 0
    isin_cerca = 0
    lblrend = 0
    lblstd = 0
    label_mav = 0

    testolabelrend = "Il rendimento medio del titolo è: "
    testolabelstd = "La dev. std è: "
    testolabelmav = "La media mobile del titolo è: "

    valuelabelrend = ""
    valuelabelstd = ""
    valuelabelmav = ""

    periodizzazione_cerca = 0
    data_sel = 0

    #reference a frame AGGIUNGI
    isin_agg = 0
    quantity_agg = 0    #input quantità
    position_agg = 0    #input posizione    0 = long 1 = short
    titolo_agg = 0     #input societa
    
    #reference a frame MODIFICA
    titolo_modifica = 0
    position_modifica = 0
    quantity_modifica = 0
    combosocieta_modifica = 0
    
    

    def __init__(self, tabmodificaport):
        
        self.modificaport = tabmodificaport

        #Creazione labelframe modulo cerca ---------------------------------------------------------------------------------CERCA
        frame_cerca = ttk.LabelFrame(self.modificaport, text = 'Overview titolo')
        frame_cerca.grid(column = 0, row = 0, sticky = "w")

        #adding a Textbox entry per l'ISIN
        self.isin_cerca = tk.StringVar() 
        insert_isin_cerca = ttk.Entry(frame_cerca, textvariable = self.isin_cerca) 
        insert_isin_cerca.grid(column = 0, row = 0)
        
        #Creazione menu a tendina elenco società        #dasostituire nome variabili
        self.titolo_cerca = tk.StringVar()
        combostrumenti_cerca = ttk.Combobox(frame_cerca, state = 'readonly', values = GLOBE.mappa_strumenti.values(), textvariable = self.titolo_cerca)
        # combotitolo_cerca['values'] = list(GLOBE.lista_NASDAQ.keys())
        combostrumenti_cerca.grid(column = 1, row = 0, sticky = "w")
        combostrumenti_cerca.current(0)

        #Creazione menu a tendina elenco periodizzazione dati   DA GUARDARE
        self.periodizzazione_cerca = tk.StringVar()
        combodata = ttk.Combobox(frame_cerca, state = 'readonly', values = GLOBE.mappa_periodicita.values(), textvariable = self.periodizzazione_cerca)
        combodata.grid(column = 2, row = 0)
        combodata.current(0)        

        #creazione entry widget per l'inserimento della data
        self.data_sel = tk.StringVar()
        self.insert_data = tk.Entry(frame_cerca)
        self.insert_data.grid(column = 3, row = 0)
        
        #adding a button CERCA
        query_cerca = ttk.Button(frame_cerca, text = "Cerca", command = self.CallBackCerca)     
        query_cerca.grid(column = 4, row = 0)

        #display rendimento e std aggiornato ogni callbackcerca
        self.valuelabelrend = tk.StringVar()
        self.valuelabelrend.set(self.testolabelrend + "0")
        self.lblrend = ttk.Label(frame_cerca, textvariable = self.valuelabelrend)
        self.lblrend.grid(column = 0, row = 2)

        self.valuelabelstd = tk.StringVar()
        self.valuelabelstd.set(self.testolabelstd + "0")
        self.lblstd = ttk.Label(frame_cerca, textvariable = self.valuelabelstd)
        self.lblstd.grid(column = 0, row = 3)

        #Creazione sub_frame destra collegato a cerca:::::::::::::::::::::::::::::::::SUB-CERCA

        frame_cerca_tech = ttk.LabelFrame(self.modificaport, text = 'Strumenti timing')
        frame_cerca_tech.grid(column = 1, row = 0, sticky = "nwe")

        self.valuelabelmav = tk.StringVar()
        self.valuelabelmav.set(self.testolabelmav + "0")
        self.label_mav = ttk.Label(frame_cerca_tech, textvariable = self.valuelabelmav)
        self.label_mav.grid(column = 0, row = 0, sticky = "nwe")



        #Creazione sub_frame destra collegato a cerca:::::::::::::::::::::::::::::::::SUB-CERCA^^^

        #Creazione labelframe modulo cerca ---------------------------------------------------------------------------------CERCA^^^

        #Creazione labelframe modulo aggiungi ******************************************************************************AGGIUNGI
     
        frame_aggiungi = ttk.LabelFrame(self.modificaport, text = 'Aggiungi titolo')
        frame_aggiungi.grid(column = 0, row = 1, sticky = "W")

        #adding a Textbox entry per l'ISIN
        self.isin_agg = tk.StringVar() 
        insert_isin_agg = ttk.Entry(frame_aggiungi, textvariable = self.isin_agg) 
        insert_isin_agg.grid(column = 0, row = 0)
        
        #Creazione menu a tendina titoli
        self.titolo_agg = tk.StringVar()
        combostrumenti_aggiungi = ttk.Combobox(frame_aggiungi, state = 'readonly', values = GLOBE.mappa_strumenti.values(), textvariable = self.titolo_agg)
        # combosocieta['values'] = list(GLOBE.lista_NASDAQ.keys())
        combostrumenti_aggiungi.grid(column = 1, row = 0)
        combostrumenti_aggiungi.current(0)

        #adding a Textbox entry per le quantità
        self.quantity_agg = tk.IntVar() # il totale dovrà essere minore del cash disponibile *da vedere*
        insertqt_agg = ttk.Entry(frame_aggiungi, textvariable = self.quantity_agg) # la quantità deve essere un intero e non inferiore a 0
        insertqt_agg.grid(column = 2, row = 0)

        #Creating radio buttons (SHORT-LONG)
        self.position_agg = tk.IntVar()

        check_longagg = tk.Radiobutton(frame_aggiungi, text = "Long", variable = self.position_agg, value = 0)     #0 = LONG
        check_longagg.select()
        check_longagg.grid(column = 0, row = 1, sticky = tk.W)
 
        check_shortagg = tk.Radiobutton(frame_aggiungi, text = "Short", variable = self.position_agg, value = 1)    #1 = SHORT
        check_shortagg.deselect()
        check_shortagg.grid(column = 1, row = 1, sticky = tk.W)
           
        #adding button inserisci
        query_aggiungi = ttk.Button(frame_aggiungi, text = "Inserisci", command = self.CallBackInserisci)
        query_aggiungi.grid(column = 3, row = 0)

        #Creazione labelframe modulo aggiungi ******************************************************************************AGGIUNGI^^^

        #Creazione labelframe modulo modifica ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MODIFICA

        frame_modifica = ttk.LabelFrame(self.modificaport, text = "Modifica portafoglio")
        frame_modifica.grid(column = 0, row = 2, sticky = "W")

        #creazione menu a tendina società
        self.titolo_modifica = tk.StringVar()
        self.combotitolo_modifica = ttk.Combobox(frame_modifica, state = 'readonly', textvariable = self.titolo_modifica)
        self.combotitolo_modifica['values'] = GLOBE.MenuTitoliPortafoglioModifica()
        self.combotitolo_modifica.grid(column = 0, row = 0)
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

        isin = self.isin_agg.get()

        tipologia_strumento = self.titolo_agg.get()    

        if GLOBE.titolo.get("isin") == None or GLOBE.titolo.get("quantity") == 0:
            
            if self.quantity_agg.get() > 0:     #controllo quantità inserita maggiore di 0

                dfp = CALLAPI.BEESCALLER().ApiGetAllByIsinPortafoglio(isin, tipologia_strumento)

                GLOBE.AggiungiTitolo(isin, dfp.get("info_gen")["full_name"].values[0], dfp.get("info_gen")["symbol"].values[0], dfp.get("tipo_strumento"), dfp.get("info_gen")["country"].values[0], self.quantity_agg.get(), self.position_agg.get(), datetime.now(), dfp.get("datafetch")["Close"].iloc[len(dfp.get("datafetch")) - 1], dfp)
                self.combotitolo_modifica['values'] = GLOBE.MenuTitoliPortafoglioModifica()

                FILE.ScritturaPortafoglioSuFile()
                    
    def CallbackModifica(self):            

        print("Callbackmodifica .......")

        nome = self.titolo_modifica.get()    

        quantita = self.quantity_modifica.get()

        isin = 0

        for i in list(GLOBE.titolo.keys()):
               if GLOBE.titolo[i].get("nome") == nome:

                   isin = GLOBE.titolo[i].get("isin")


        if quantita == 0:       #se la quantità inserita in modifica è 0, si tramuta in un'eliminaizone dal portafoglio
   
           del GLOBE.titolo[isin]

           self.combotitolo_modifica['values'] = GLOBE.MenuTitoliPortafoglioModifica()
           self.combotitolo_modifica.current(0)

        elif quantita >= GLOBE.titolo[isin].get("quantity"):

            msg.showerror("Errore", "Sono ammesse solo operazioni di vendita")
            return 
            
        else:

            GLOBE.titolo.get(isin)["quantity"] = quantita
            

        FILE.ScritturaPortafoglioSuFile()

    def CallBackCerca(self):

        print("CallbackCerca.....")
        
        periodizzazione = self.periodizzazione_cerca.get()

        data_dati = self.insert_data.get()

        tipo_strumento = self.titolo_cerca.get()    #restituisce il simbolo associato al nome inviato a Lista_NASDQ

        isin = self.isin_cerca.get()

        df = CALLAPI.BEESCALLER().ApiGetAllByIsin(isin, tipo_strumento, periodizzazione, data_dati)

        self.valuelabelrend.set(self.testolabelrend + str(CALC.DeltaChangeAvg(df, 'Close')))
        self.valuelabelstd.set(self.testolabelstd + str(CALC.DeltaChangeStd(df, 'Close')))
        
        PLOT.PLOTFACTORY().SubPlotLineeBarre(df.get("info_gen")["symbol"].values[0], df.get("datafetch"), 'Close', 10, 5, 5)

        if tipo_strumento == GLOBE.mappa_strumenti.get("Stock"):    #primo parametro simbolo

            self.valuelabelmav.set(self.testolabelmav + str(CALC.MovingAvgCerca(df.get("info_gen")["symbol"].values[0], df.get("info_gen")["country"].values[0], tipo_strumento, periodizzazione)))
        else:           #primo parametro != symbol

            self.valuelabelmav.set(self.testolabelmav + str(CALC.MovingAvgCerca(df.get("info_gen")["full_name"].values[0], df.get("info_gen")["country"].values[0], tipo_strumento, periodizzazione)))