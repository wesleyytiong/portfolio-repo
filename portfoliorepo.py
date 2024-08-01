"""
Portfolio Optimization
"""

import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf

#Import data
def getData(stocks, start, end):
    #Download stock data using yfinance
    stockData = yf.download(stocks, start = start, end = end)
    
    #Store 'Close' prices for calculations
    stockData = stockData['Close']
    
    #Calculate percent change (returns)
    returns = stockData.pct_change()
    
    #Calculate mean returns
    meanReturns = returns.mean()

    #Calculate covariance matrix
    covMatrix = returns.cov()
    return meanReturns, covMatrix

#Define parameters
stocks = ['AAPL', 'NVDA', 'META']
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=365)

data = getData(stocks, start=startDate, end=endDate)
print(data)
