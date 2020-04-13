import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

import pandas as pd
import pandas_datareader.data as web

from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
from datetime import timedelta

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
years_fmt = mdates.DateFormatter('%m')


start = datetime(2020, 3, 2)
end = datetime.now()

df = web.DataReader("AAPL", "av-daily-adjusted", start, end, api_key = 'OQ5SXA6KT34O569F')




fig, ax = plt.subplots()

ax.plot(df, df["adjusted close"])

# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)

# round to nearest years.
datemin = start - timedelta(15)
datemax = end
ax.set_xlim(datemin, datemax)

# format the coords message box
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.format_ydata = lambda x: '$%1.2f' % x  # format the price.
ax.grid(True)

# rotates and right aligns the x labels, and moves the bottom of the
# axes up to make room for them
fig.autofmt_xdate()

plt.show()