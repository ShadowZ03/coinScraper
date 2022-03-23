import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests
#####
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import matplotlib.dates as mpl_dates
###


# Extracting Data for plotting
data = pd.read_csv(r"C:\Users\Dmitri Gatto\Downloads\MATIC-USD.csv", index_col=0, parse_dates=True)
del data['Adj Close']
data.index.name = 'Date'
data.shape
print(data.head())

mpf.plot(data, type='candle', show_nontrading=True, title='Hello', hlines=[2,2.54])