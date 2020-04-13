import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
import json
from datetime import datetime
from datetime import timedelta


import Plot_factory as PLOT   #Chiamata plotting
import View_manager as MANAGER

import globalita as GLOBE
import API_call as CALLAPI
import InterpreterAPI as INTPR
import Lavoro_file as FILE


GLOBE.CaricaNASDAQ()
FILE.LetturaPortFile()

CALLAPI.BEESCALLER().ChiamataApiPortafoglioPanoramica()


viewmanager = MANAGER.VIEWMANAGER()




viewmanager.win.update()
viewmanager.win.deiconify()
viewmanager.win.mainloop()         


#TODO aggiornamento dei risultati portafoglio rend dev ecc con cambio tab
#TODO da sistemare i dropna() nel calcolo change

