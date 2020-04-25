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
import Tooltip as TIP

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
    testolabelmav = "La media mobile del titolo è: \n"
    testolabelprice = "Il prezzo attuale è: "

    valuelabelprice = ""
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
        frame_cerca.grid(column = 0, row = 0, pady = 20, sticky = "nws")

        #adding a Textbox entry per l'ISIN
        self.isin_cerca = tk.StringVar() 
        insert_isin_cerca = ttk.Entry(frame_cerca, textvariable = self.isin_cerca) 
        insert_isin_cerca.grid(column = 0, row = 0, padx = 20)
        TIP.TOOLTIP(insert_isin_cerca, "Inserisci qui l'isin dello strumento che vuoi cercare. Controlla di non aver inserito spazi vuoti alla fine!")
        
        #Creazione menu a tendina elenco società        #dasostituire nome variabili
        self.titolo_cerca = tk.StringVar()
        combostrumenti_cerca = ttk.Combobox(frame_cerca, state = 'readonly', values = list(GLOBE.mappa_strumenti), textvariable = self.titolo_cerca)
        # combotitolo_cerca['values'] = list(GLOBE.lista_NASDAQ.keys())
        combostrumenti_cerca.grid(column = 1, row = 0, padx = 20)
        combostrumenti_cerca.current(0)
        TIP.TOOLTIP(combostrumenti_cerca, "Seleziona il tipo di strumento che vuoi cercare")

        #Creazione menu a tendina elenco periodizzazione dati  
        self.periodizzazione_cerca = tk.StringVar()
        combodata = ttk.Combobox(frame_cerca, state = 'readonly', values = list(GLOBE.mappa_periodicita), textvariable = self.periodizzazione_cerca)
        combodata.grid(column = 2, row = 0, padx = 20)
        combodata.current(0)        
        TIP.TOOLTIP(combodata, "Seleziona la periodizzazione delle osservazioni")

        #creazione entry widget per l'inserimento della data
        self.data_sel = tk.StringVar()
        self.insert_data = tk.Entry(frame_cerca)
        self.insert_data.grid(column = 3, row = 0, padx = 20)
        TIP.TOOLTIP(self.insert_data, "Inserisci la data da cui vuoi partire con le osservazioni, il formato deve essere gg/mm/ANNO")
        
        #adding a button CERCA
        query_cerca = ttk.Button(frame_cerca, text = "Cerca", command = self.CallBackCerca)     
        query_cerca.grid(column = 4, row = 0, padx = 20)

        #Creazione sub_frame destra collegato a cerca:::::::::::::::::::::::::::::::::SUB-CERCA

        frame_cerca_tech = ttk.LabelFrame(self.modificaport, text = 'Strumenti timing')
        frame_cerca_tech.grid(column = 1, row = 0, pady = 20, sticky = "nwe")

        #display rendimento e std aggiornato ogni callbackcerca
        self.valuelabelprice = tk.StringVar()
        self.valuelabelprice.set(self.testolabelprice + "0")
        self.lblprice = ttk.Label(frame_cerca_tech, textvariable = self.valuelabelprice)
        self.lblprice.grid(column = 0, row = 0, sticky = "nswe")

        self.valuelabelrend = tk.StringVar()
        self.valuelabelrend.set(self.testolabelrend + "0")
        self.lblrend = ttk.Label(frame_cerca_tech, textvariable = self.valuelabelrend)
        self.lblrend.grid(column = 0, row = 1, sticky = "nswe", pady = 10)

        self.valuelabelstd = tk.StringVar()
        self.valuelabelstd.set(self.testolabelstd + "0")
        self.lblstd = ttk.Label(frame_cerca_tech, textvariable = self.valuelabelstd)
        self.lblstd.grid(column = 0, row = 2, sticky = "nswe")
        TIP.TOOLTIP(self.lblstd, "La deviazione standard è un indice di rischio del titolo, a parità di rendimento si preferisce una dev.std minore")

        self.valuelabelmav = tk.StringVar()
        self.valuelabelmav.set(self.testolabelmav + "0")
        self.label_mav = ttk.Label(frame_cerca_tech, textvariable = self.valuelabelmav)
        self.label_mav.grid(column = 0, row = 3, sticky = "nswe", pady = 10)
        TIP.TOOLTIP(self.label_mav, "La media mobile è un segnale che permette di identificare i momenti in cui entrare nell'investimento. Bisogna sempre tenere conto degli obiettivi a lungo termine dell'investimento da rapportare al segnale opportuno")


        #Creazione sub_frame destra collegato a cerca:::::::::::::::::::::::::::::::::SUB-CERCA^^^
        #Creazione labelframe modulo cerca ---------------------------------------------------------------------------------CERCA^^^

        #Creazione labelframe modulo aggiungi ******************************************************************************AGGIUNGI
     
        frame_aggiungi = ttk.LabelFrame(self.modificaport, text = 'Aggiungi titolo')
        frame_aggiungi.grid(column = 0, row = 1, pady = 20, sticky = "nw")
        

        #adding a Textbox entry per l'ISIN
        self.isin_agg = tk.StringVar() 
        insert_isin_agg = ttk.Entry(frame_aggiungi, textvariable = self.isin_agg) 
        insert_isin_agg.grid(column = 0, row = 0, padx = 20)
        TIP.TOOLTIP(insert_isin_agg, "Inserisci qui l'isin dello strumento che vuoi aggiungere in portafoglio. Controlla di non aver inserito spazi vuoti alla fine!")
        
        #Creazione menu a tendina titoli
        self.titolo_agg = tk.StringVar()
        combostrumenti_aggiungi = ttk.Combobox(frame_aggiungi, state = 'readonly', values = list(GLOBE.mappa_strumenti), textvariable = self.titolo_agg)
        # combosocieta['values'] = list(GLOBE.lista_NASDAQ.keys())
        combostrumenti_aggiungi.grid(column = 1, row = 0, padx = 20)
        combostrumenti_aggiungi.current(0)
        TIP.TOOLTIP(combostrumenti_aggiungi, "Seleziona il tipo di strumento.")

        #adding a Textbox entry per le quantità
        self.quantity_agg = tk.IntVar() # il totale dovrà essere minore del cash disponibile *da vedere*
        insertqt_agg = ttk.Entry(frame_aggiungi, textvariable = self.quantity_agg) # la quantità deve essere un intero e non inferiore a 0
        insertqt_agg.grid(column = 2, row = 0, padx = 20)
        TIP.TOOLTIP(insertqt_agg, "Inserisci la quantità da acquistare.")
         
        #adding button inserisci
        query_aggiungi = ttk.Button(frame_aggiungi, text = "Inserisci", command = self.CallBackInserisci)
        query_aggiungi.grid(column = 3, row = 0, padx = 20)

        #Creazione labelframe modulo aggiungi ******************************************************************************AGGIUNGI^^^

        #Creazione labelframe modulo modifica ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MODIFICA

        frame_modifica = ttk.LabelFrame(self.modificaport, text = "Modifica portafoglio")
        frame_modifica.grid(column = 0, row = 2, pady = 20, sticky = "nw")

        #creazione menu a tendina società
        self.titolo_modifica = tk.StringVar()
        self.combotitolo_modifica = ttk.Combobox(frame_modifica, state = 'readonly', textvariable = self.titolo_modifica)
        self.combotitolo_modifica['values'] = GLOBE.MenuTitoliPortafoglioModifica()
        self.combotitolo_modifica.grid(column = 0, row = 0, padx = 20)
        TIP.TOOLTIP(self.combotitolo_modifica, "Seleziona quale strumento vuoi modificare.")
        # combosocieta_modifica.current()

        #adding a Textbox entry per le quantità
        self.quantity_modifica = tk.IntVar() # il totale dovrà essere minore del cash disponibile *da vedere*
        insertqt_mod = ttk.Entry(frame_modifica, textvariable = self.quantity_modifica) # la quantità deve essere un intero e non inferiore a 0
        insertqt_mod.grid(column = 1, row = 0, padx = 20)
        TIP.TOOLTIP(insertqt_mod, "-Inserisci 0 se vuoi vendere lo strumento selezionato. \n-Inserisci un valore minore della quantità totale per venderne solo una parte. \n-Non sono ammesse modifiche in acquisto.")

        #adding a button
        query_modifica = ttk.Button(frame_modifica, text = "Modifica", command = self.CallbackModifica)
        query_modifica.grid(column = 3, row = 0, padx = 20)
         #Creazione labelframe modulo modifica ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MODIFICA^^^    

    def CallBackInserisci(self):
        
        print("Callbackinserisci .......")

        isin = self.isin_agg.get()

        tipologia_strumento = self.titolo_agg.get()    


        soglia_beta = 1.4
        soglia_risk_rating = 3

        if GLOBE.titolo.get("isin") == None or GLOBE.titolo.get("quantity") == 0:
            
            if self.quantity_agg.get() > 0 and GLOBE.country_isin.get(isin[:2]) != None:     #controllo quantità inserita maggiore di 0

                dfp = CALLAPI.BEESCALLER().ApiGetAllByIsinPortafoglio(isin, tipologia_strumento)

                if GLOBE.profilazione == "Livello Basso" and (dfp.get("info_tech").get("Beta") >= soglia_beta or dfp.get("info_tech").get("Risk Rating") >= soglia_risk_rating): #controllo profilazione

                    msg.showwarning(title = "Informazioni investimento", message = "Il grado di rischio di questo strumento non è adatto al suo portafoglio.")

                    return

                if len(dfp.get("datafetch")) < 60:

                    msg.showwarning(title = "Mancanza dati", message = "Le osservazioni non permettono un calcolo del beta adeguato.")

                    return
                    
                GLOBE.AggiungiTitolo(isin, dfp.get("info_gen")["name"].values[0], dfp.get("info_gen")["symbol"].values[0], 
                                        dfp.get("tipo_strumento"), dfp.get("info_gen")["country"].values[0], self.quantity_agg.get(), 
                                        datetime.now(), dfp.get("datafetch")["Close"].iloc[len(dfp.get("datafetch")) - 1], dfp)
                
                msg.showinfo(title = "Moviementazione eseguita", message = "Operazione eseguita con successo")

                self.combotitolo_modifica['values'] = GLOBE.MenuTitoliPortafoglioModifica()

                FILE.ScritturaPortafoglioSuFile()
            else:

                msg.showwarning(title = "Problema inserimento", message = "Controlla di aver inserito correttamente l'isin o la quantità")

                return
                    
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

           msg.showinfo(title = "Movimentazione eseguita", message = f"Operazione eseguita con successo, hai venduto tutto lo stock!")

        elif quantita >= GLOBE.titolo[isin].get("quantity"):

            msg.showerror("Errore", "Sono ammesse solo operazioni di vendita")
            return 
            
        else:

            GLOBE.titolo.get(isin)["quantity"] = quantita
            msg.showinfo(title = "Movimentazione eseguita", message = f"Operazione eseguita con successo, ora ne possiedi {quantita}")
            

        FILE.ScritturaPortafoglioSuFile()

    def CallBackCerca(self):

        print("CallbackCerca.....")
        
        periodizzazione = self.periodizzazione_cerca.get()

        data_dati = self.insert_data.get()

        tipo_strumento = self.titolo_cerca.get()    #restituisce il simbolo associato al nome inviato a Lista_NASDQ

        isin = self.isin_cerca.get()

        if GLOBE.country_isin.get(isin[:2]) == None:

            msg.showwarning(title = "Problema inserimento", message = "Controlla di aver inserito correttamente l'isin")

            return

        df = CALLAPI.BEESCALLER().ApiGetAllByIsin(isin, tipo_strumento, periodizzazione, data_dati)

        self.valuelabelprice.set(self.testolabelprice + str(round(df.get("datafetch")["Close"].iloc[-1], 2)))
        self.valuelabelrend.set(self.testolabelrend + str(round(CALC.DeltaChangeAvg(df, 'Close'), 2)))
        self.valuelabelstd.set(self.testolabelstd + str(round(CALC.DeltaChangeStd(df, 'Close'), 2)))
        self.valuelabelmav.set(self.testolabelmav + str(CALC.MovingAvgCerca(df, tipo_strumento, periodizzazione)))

        PLOT.PLOTFACTORY().SubPlotLineeBarre(df, 'Close', 10, 5, 5)

        
        # if tipo_strumento == GLOBE.mappa_strumenti.get("stock"):    #primo parametro simbolo

        #     self.valuelabelmav.set(self.testolabelmav + str(CALC.MovingAvgCerca(df.get("info_gen")["symbol"].values[0], df.get("info_gen")["country"].values[0], tipo_strumento, periodizzazione)))
            
        # else:           #primo parametro != symbol

        #     self.valuelabelmav.set(self.testolabelmav + str(CALC.MovingAvgCerca(df.get("info_gen")["full_name"].values[0], df.get("info_gen")["country"].values[0], tipo_strumento, periodizzazione)))

        