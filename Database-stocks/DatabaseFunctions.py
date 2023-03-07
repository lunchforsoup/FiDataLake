from sys import argv

import pandas as pd
import yfinance as yf
import sqlite3

con= sqlite3.connect('C:\git\FiDataLake\market_data.sqlite')

def get_stock_data(symbol,start,end):
    df = yf.download(symbol,start=start,end=end)
    df.reset_index(inplace=True)
    df.rename(columns={
        'Date':'date',
        'Open':'open',
        'High':'high',
        'Low':'low',
        'Close':'close',
        'Adj Close':'adj_close',
        'Volume':'volume'
        },inplace=True)
    df['symbol'] = symbol
    return df


def save_stock_data(symbol,start,end):
    data= get_stock_data(symbol,start,end)
    data.to_sql('stock_data',con=con,if_exists='append',index=False)

def save_last_trading_session(symbol):
    today = pd.timestamp.today()
    data= get_stock_data(symbol,today,today)
    data.to_sql('stock_data ',con=con,if_exists='append',index=False)





save_stock_data('','2010-01-01','2020-01-01')


lkk.read_sql('select * from stock_data',con=con)

