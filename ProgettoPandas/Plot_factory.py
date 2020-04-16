import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import matplotlib as mpl

from matplotlib import style
import Metodi_calcolo as CALC
import Modificaport_ctrl as MODCTRL
           

class PLOTFACTORY():
  
    def SubPlotLineeBarre(self, symbol, dataframe, recordtype, mavglenght, figlenght, figheight):
        
        plt.close('all')    #chiusura di tutti i grafici
       
        # Adjusting the style of matplotlib
        style.use('ggplot')
        # plt.xticks(np.arange(0, 30, step=5)) 

        recordY = dataframe.get("datafetch")[recordtype] #selezione colonna

        fig = plt.figure(1, clear = True)
        ax = fig.add_subplot(121)
        ax1 = fig.add_subplot(122)

        
        fig.autofmt_xdate()
    
        #plot 1 L-------------------------------------
        mavg = recordY.rolling(window= mavglenght).mean()
        ax.plot(recordY, label = symbol)
        ax.plot(mavg, label = 'Media Mobile')
        ax.set_title(str(symbol) + " prices data")
        #plot 1 L-------------------------------------

        #plot 2 R-------------------------------------
        rendimento = CALC.DeltaChange(dataframe, recordtype)
        ax1.plot(rendimento, label = symbol)
        ax1.set_title(str(symbol) + " returns data")
        #plot 2 R-------------------------------------
        
        plt.show()  #da togliere quando inserito nel canvas

        


        



        
