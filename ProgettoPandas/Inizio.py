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
import Lavoro_file as FILE

FILE.LetturaDaProfilazione()
FILE.LetturaPortafoglioDaFile()

CALLAPI.BEESCALLER().ChiamataApiPortafoglioPanoramica()


viewmanager = MANAGER.VIEWMANAGER()



viewmanager.win.update()
viewmanager.win.deiconify()
viewmanager.win.mainloop()         


#TODO aggiornamento dei risultati portafoglio rend dev ecc con cambio tab
#TODO trovare un modo per restituire il risk rating e il beta tramite lo stesso array
#TODO guardare ilò problema degli int nel calcolo quoziente
#TODO Abbellire i form 


