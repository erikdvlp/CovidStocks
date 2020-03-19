from bs4 import BeautifulSoup
import requests as r
import commodity as c

def scrape():
	#DOW
	dow = c.Commodity("Dow Jones Industrial Average", "https://money.cnn.com/data/markets/dow/", 29568.57)
	page = BeautifulSoup(r.get(dow.src).content, 'html.parser')
	raw = page.find("td", {"class": "wsod_last wsod_lastIndex"}).findAll("span")
	dow.price = float(raw[0].text.replace(',',''))
	dow.time = raw[1].text[:-3]
	dow.calcDiff()
	dow.format()

	#TSX
	tsx = c.Commodity("S&P/TSX Composite Index", "https://www.theglobeandmail.com/investing/markets/indices/", 17970.50)
	page = BeautifulSoup(r.get(tsx.src).content, 'html.parser')
	raw = page.find("span", {"class": "barchart-overview-field-value"}).find("barchart-field").attrs['value']
	tsx.price = float(raw.replace(',',''))
	tsx.calcDiff()
	tsx.format()

	results = [dow, tsx]
	return results