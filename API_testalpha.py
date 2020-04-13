from alpha_vantage.timeseries import TimeSeries
# Your key here
key = 'OQ5SXA6KT34O569F'
ts = TimeSeries(key)


aapl, meta = ts.get_daily(symbol='AAPL')
print(aapl)