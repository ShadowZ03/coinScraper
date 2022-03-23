import requests
from bs4 import BeautifulSoup
import json

mystocks = ['AAVE', 'BTC', 'MATIC', 'DOT', 'VGX', 'ADA', 'XLM']
stockdata = []

def getData(symbol):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
    url3 = f'https://finance.yahoo.com/quote/{symbol}-USD'
    r = requests.get(url3, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    stock = {
        'symbol': symbol,
        'currentPrice': soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('fin-streamer')[0].text,
        'priceChange': soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[0].text,
        'percentChange': soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[1].text,
        'volume': soup.find("div", {"class": "D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)"}).find_all('tr')[-3].text,
    }
    return stock

for item in mystocks:
    stockdata.append(getData(item))
    print('Getting: ', item)

with open('stockdata.json', 'w') as f:
    json.dump(stockdata, f)

print('fin')

  