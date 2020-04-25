import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import globalita as GLOBE
import API_call as CALLAPI
import Panoramica_ctrl as PANCTRL
import Modificaport_ctrl as MODCTRL
import Questionario_ctrl as QUESTCTRL
import Consulente_ctrl as CONSCTRL
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
    consctrl = 0
    questctrl = 0
    
    def __init__(self):
        
        self.win = tk.Tk()
        # self.win = tk.ThemedTk()
        self.win.title("ROBOCOOP")

        # self.win.get_themes()
        # self.win.set_theme("Equilux")

        self.tabControl = ttk.Notebook(self.win)
        
    
        #Add tab PANORAMICA
        self.panoramica = ttk.Frame(self.tabControl)
        self.tabControl.add(self.panoramica, text = 'Panoramica', state = self.DisableTab())

        #Add tab MODIFICAPORT
        self.modificaport = ttk.Frame(self.tabControl)
        self.tabControl.add(self.modificaport, text = 'Modifica/Aggiungi', state = self.DisableTab())

        #Add tab CONSULENTE
        self.consulente = ttk.Frame(self.tabControl)
        self.tabControl.add(self.consulente, text = 'Consulente', state = self.DisableConsulente())

        #Add tab QUESTIONARIO
        self.questionario = ttk.Frame(self.tabControl)
        self.tabControl.add(self.questionario, text = 'Questionario', state = self.DisableQuestionario())

        self.tabControl.pack(expand = 1, fill = 'both') 

        self.panctrl = PANCTRL.PANORAMICACTRL(self.panoramica)

        self.questctrl = QUESTCTRL.QUESTIONARIOCTRL(self.questionario)

        self.modctrl = MODCTRL.MODIFICAPORTCTRL(self.modificaport)

        self.consctrl = CONSCTRL.CONSULENTECTRL(self.consulente)

        self.tabControl.bind("<<NotebookTabChanged>>", self.CambioTab)
        
    def CambioTab(self, event):

        selection = event.widget.select()
        tab = event.widget.tab(selection, "text")
        # print("text:", tab)
        print(f"Cambio alla tab {tab}, i titoli sono: {GLOBE.titolo.keys()}")
        if  tab == "Panoramica":
       
            TAB.Tabella(self.panctrl.frame_port)
            self.panctrl.SetPanoramicaTechValues()
        
        elif tab == "Consulente":

            self.consctrl.SetConsulenteValues()

    def DisableTab(self):

        if GLOBE.profilazione == False:

            return "disabled"
            
        else:

            return "normal"
    
    def DisableQuestionario(self):

        if GLOBE.profilazione != False:

            return "hidden"

        else:

            return "normal"
            
    def DisableConsulente(self):

        if not GLOBE.titolo or GLOBE.profilazione == False:

            return "disabled"
        
        else:

            return "normal"
            