
from datetime import datetime
from datetime import timedelta
from tkinter import messagebox

import globalita as GLOBE

# def GetDailyByDateRange(da_from, a_to):
#     #fare controllo minoritù
#     result = {}

#     # if da_from >= a_to:     #da controllare la validità del controllo
    
#     #     messagebox.showerror("Error", "La data inserita deve essre passato-recente")
        
           
#     while da_from <= a_to:

#         datekey = da_from.strftime("%Y-%m-%d")
#         #todo controllo sul none del daily
#         value = GLOBE.societa.get('daily').get(datekey) 

#         if value != None:

#             result[datekey] = value

#         da_from = da_from + timedelta(days = 1)

#     return result

def GetObsByKey(array, item):   #array come df da web, item come key della colonna es. 'close', 'open'

    record = array[item]

    return  record

