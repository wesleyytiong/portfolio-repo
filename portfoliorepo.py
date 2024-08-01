"""
Portfolio Optimization
"""

import numpy as np
import datetime as dt
import yfinance as yf
from pandas_datareader import data as pdr

#Import data
def getData(stocks, start, end):
    stockData = yf.download(stocks, start = start, end = end)
    stockData = stockData['Close']
    
#From data, output returns as percent change, mean returns, and covariance matrix
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix

#Define parameters
stocks = ['AAPL', 'NVDA', 'META']

endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=365)

data = getData(stocks, start=startDate, end=endDate)
print(data)
