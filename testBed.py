import requests
from bs4 import BeautifulSoup
import json

mystocks = ['AAVE', 'BTC', 'MATIC', 'DOT', 'VGX', 'ADA', 'XLM']
stockdata = []


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
url3 = f'https://finance.yahoo.com/quote/BTC-USD'
r = requests.get(url3, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

currentPrice = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('fin-streamer')[0].text
priceChange = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[0].text
percentChange = soup.find("div", {"class": "D(ib) Mend(20px)"}).find_all('span')[1].text
volume = soup.find("div", {"class": "D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)"}).find_all('tr')[-3].text

print(volume)
#<div class="D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)" data-test="right-summary-table"><table class="W(100%) M(0) Bdcl(c)"><tbody><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Market Cap</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="MARKET_CAP-value">702.841B</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Circulating Supply</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="CIRCULATING_SUPPLY-value">18.94M</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Max Supply</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="MAX_SUPPLY-value">N/A</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Volume</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="TD_VOLUME-value"><fin-streamer data-symbol="BTC-USD" data-field="regularMarketVolume" data-trend="none" data-pricehint="2" data-dfield="longFmt" value="23,719,858,176" active=""><span class="_11248a25 _8e5a1db9">23,650,236,416</span></fin-streamer></td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) "><td class="C($primaryColor) W(51%)"><span>Volume (24hr)</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="TD_VOLUME_24HR-value">23.72B</td></tr><tr class="Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) Bdbw(0)! "><td class="C($primaryColor) W(51%)"><span>Volume (24hr) All Currencies</span></td><td class="Ta(end) Fw(600) Lh(14px)" data-test="TD_VOLUME_24HR_ALLCURRENCY-value">23.72B</td></tr></tbody></table></div>