import os

import matplotlib
import pandas as pd
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates
import tkinter as tk
from tkinter import ttk
import investpy as inv


from pandas import DataFrame
from matplotlib import style
from datetime import datetime
from datetime import timedelta
import statsmodels.api as sm
from prettytable import PrettyTable

import API_call as CALLAPI
import Metodi_calcolo as CALC
import globalita as GLOBE




# res = inv.stocks.get_stocks_overview("united states", as_json=False, n_results=50)
# print(res)

# isin = inv.stocks.search_stocks("country", "italy")
# print(isin)

info = inv.stocks.get_stock_information("aapl", "united states", as_json=False)
print(info["Beta"])