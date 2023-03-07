import pandas as pd
import numpy as np
import yfinance as yf
from scipy.stats import gmean

import matplotlib.pyplot as plt
import seaborn as sns

import warnings
import gc

#get data

item={}
tickerStrings = ['spy', 'MSFT']
df_list = list()
for ticker in tickerStrings:
    data = yf.download(ticker, group_by="Ticker")
    data['ticker'] = ticker  # add this column because the dataframe doesn't contain a column with the ticker
    df_list.append(data)

# combine all dataframes into a single dataframe
df1 = pd.concat(df_list)



# save to csv
df1.to_csv('ticker.csv')





#Create calculations
