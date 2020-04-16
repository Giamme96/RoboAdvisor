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

# isin = inv.stocks.search_stocks("isin", "US4642872349")
# print(isin)

# info = inv.stocks.get_stock_information("aapl", "united states", as_json=False)
# print(info["Beta"])

# info = CALLAPI.BEESCALLER().ApiCallInfoStock("aapl")
# print(info)

fund = inv.funds.get_funds(country="united states")
print(fund)
# byvalue = fund.loc[fund["isin"] == "US9229087104"]
# print(byvalue)
# etfs = inv.etfs.get_etfs(country="united states")
# byvalue_etf = etfs.loc[etfs["isin"] == "US25459W1027"]
# print(byvalue_etf)

# detf = CALLAPI.BEESCALLER().ApiCallByIsinPortafoglio("US25459W1027", "ETF")
# print(detf)
# isin = "US0378331005"
# tipologia_strumento = "Stock"
# stockss = inv.stocks.get_stocks(country="italy")
# byvalue_stockss = stockss.loc[stockss["isin"] == "IT0003132476"]
# print(byvalue_stockss)

# CALC.GetCountryByIsin("IT0003132476")

# country_stock = CALC.GetCountryByIsin("IT0003132476")
# stock = inv.stocks.get_stocks(country = country_stock)
# by_isin_value_to_symbol = stock.loc[stock["isin"] == "IT0003132476"]["symbol"].values[0]
# print(by_isin_value_to_symbol)

# df = CALLAPI.BEESCALLER().ApiCallByIsin("US9229087104", "Monthly", "01/01/2020", "Fund")
# print(df)

# crypto = inv.crypto.get_cryptos_dict(columns=None, as_json=False)
# print(crypto.get("name") == "BTC")

# get_info = CALC.GetInfoGenByIsin(isin, tipologia_strumento)
# stock = inv.stocks.get_stocks(country = country)
# info_gen = stock.loc[stock["isin"] == isin]
# print(get_info[1])


info = inv.funds.get_fund_information(" Gmo Emerging Markets Fund Class Vi", country = "united states", as_json=False)
print(info)