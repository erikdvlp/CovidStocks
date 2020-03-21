from bs4 import BeautifulSoup
import requests as r
import commodity as c

def scrape():
	#DOW
	dow = c.Commodity("Dow Jones Industrial Average", "index", "https://money.cnn.com/data/markets/dow/", 29568.57)
	page = BeautifulSoup(r.get(dow.src).content, 'html.parser')
	raw = page.find("td", {"class": "wsod_last wsod_lastIndex"}).findAll("span")
	dow.price = float(raw[0].text.replace(',',''))
	#dow.time = raw[1].text[:-3]
	dow.calcDiff()
	dow.format()

	#TSX
	tsx = c.Commodity("S&P/TSX Composite Index", "index", "https://www.theglobeandmail.com/investing/markets/indices/", 17970.50)
	page = BeautifulSoup(r.get(tsx.src).content, 'html.parser')
	raw = page.find("span", {"class": "barchart-overview-field-value"}).find("barchart-field").attrs['value']
	tsx.price = float(raw.replace(',',''))
	tsx.calcDiff()
	tsx.format()

	#TD
	td = c.Commodity("Toronto-Dominion Bank", "stock", "https://www.theglobeandmail.com/investing/markets/stocks/TD-T/", 77.96)
	page = BeautifulSoup(r.get(td.src).content, 'html.parser')
	raw = page.find("span", {"class": "barchart-overview-field-value"}).find("barchart-field").attrs['value']
	td.price = float(raw.replace(',',''))
	td.calcDiff()
	td.format()

	#CNR
	cnr = c.Commodity("Canadian National Railway Co.", "stock", "https://www.theglobeandmail.com/investing/markets/stocks/CNR-T/", 127.96)
	page = BeautifulSoup(r.get(cnr.src).content, 'html.parser')
	raw = page.find("span", {"class": "barchart-overview-field-value"}).find("barchart-field").attrs['value']
	cnr.price = float(raw.replace(',',''))
	cnr.calcDiff()
	cnr.format()

	#ENB
	enb = c.Commodity("Enbridge Inc.", "stock", "https://www.theglobeandmail.com/investing/markets/stocks/ENB-T/", 57.32)
	page = BeautifulSoup(r.get(enb.src).content, 'html.parser')
	raw = page.find("span", {"class": "barchart-overview-field-value"}).find("barchart-field").attrs['value']
	enb.price = float(raw.replace(',',''))
	enb.calcDiff()
	enb.format()

	#BCE
	bce = c.Commodity("Bell Canada", "stock", "https://www.theglobeandmail.com/investing/markets/stocks/BCE-T/", 65.45)
	page = BeautifulSoup(r.get(bce.src).content, 'html.parser')
	raw = page.find("span", {"class": "barchart-overview-field-value"}).find("barchart-field").attrs['value']
	bce.price = float(raw.replace(',',''))
	bce.calcDiff()
	bce.format()

	results = [dow, tsx, td, cnr, bce, enb]
	return results