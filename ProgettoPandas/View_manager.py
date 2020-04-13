import tkinter as tk
from tkinter import ttk
import globalita as GLOBE
import API_call as CALLAPI
import Panoramica_ctrl as PANCTRL
import Modificaport_ctrl as MODCTRL
import Questionario_ctrl as QUESTCTRL
import Tabella as TAB

class VIEWMANAGER():

    win = 0
    tabControl = 0

    #Reference alle tabs 
    panoramica = 0
    modificaport = 0
    consulente = 0
    questionario = 0

    panctrl = 0
    modctrl = 0
    questctrl = 0
    
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("ROBOCOOP")

        self.tabControl = ttk.Notebook(self.win)
        

        #Add tab PANORAMICA
        self.panoramica = ttk.Frame(self.tabControl)
        self.tabControl.add(self.panoramica, text = 'Panoramica')

        #Add tab MODIFICAPORT
        self.modificaport = ttk.Frame(self.tabControl)
        self.tabControl.add(self.modificaport, text = 'Modifica/Aggiungi')

        #Add tab CONSULENTE
        self.consulente = ttk.Frame(self.tabControl)
        self.tabControl.add(self.consulente, text = 'Consulente')

        #Add tab QUESTIONARIO
        self.questionario = ttk.Frame(self.tabControl)
        self.tabControl.add(self.questionario, text = 'Questionario')

        self.tabControl.pack(expand = 1, fill = 'both') 

        self.panctrl = PANCTRL.PANORAMICACTRL(self.panoramica)

        self.modctrl = MODCTRL.MODIFICAPORTCTRL(self.modificaport)

        self.questctrl = QUESTCTRL.QUESTIONARIOCTRL(self.questionario)

        self.tabControl.bind("<<NotebookTabChanged>>", self.CambioTab)
        
    def CambioTab(self, event):

        selection = event.widget.select()
        tab = event.widget.tab(selection, "text")
        # print("text:", tab)
        print(f"Cambio alla tab {tab}, società è: {GLOBE.societa.keys()}")
        if  tab == "Panoramica":
       
            TAB.Tabella(self.panctrl.frame_port)