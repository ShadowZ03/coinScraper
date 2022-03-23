import re
import json
import csv
from io import StringIO
from this import d
from bs4 import BeautifulSoup
import requests
import pandas as pd

#import csv, indexed by Date
df = pd.read_csv(r"C:\Users\Dmitri Gatto\Downloads\MATIC-USD.csv")
#index_col = 'Date'

print('_' * 50)
print(df.head())
print('_' * 50)

#Filter for Volume
print(df['Volume'] > 1210619278)
print('_' * 50)

##date Ranger
Datef = (df.loc['2022-01-01':'2022-01-06'])
print('_' * 50)

print(df.columns)
print('_' * 50)

filt = (df['Volume'] > 1210619278) & (df['Close'] > 1.6)
print('_' * 50)

print(df.loc[filt, 'High'])

print('_' * 50)
print('_' * 50)
print('_' * 50)

dateRange = (df['Date'] > '2022-01-01') & (df['Date'] < '2022-02-01')
highPrice = (df['High'] >  2)
Vol = (df['Volume'] > 1475708073)
#Uses filter highPrice, and returns Volume, Low, and Close
print(df.loc[highPrice, ['Volume', 'Low', 'Close']])

print('_' * 50)
print('_' * 50)
print('_' * 50)

#filter Data by two different filters
print(df[dateRange & highPrice & Vol])
