from bs4 import BeautifulSoup
import requests
import commodity as c

def scrape():
	#DOW Jones
	dow = c.Commodity("DOW", "https://money.cnn.com/data/markets/dow/", 29568.57)
	page = BeautifulSoup(requests.get(dow.src).content, 'html.parser')
	raw = page.find("td", {"class": "wsod_last wsod_lastIndex"}).findAll("span")
	dow.price = float(raw[0].text.replace(',',''))
	dow.time = raw[1].text
	dow.calcDiff()

	#TSX
	tsx = c.Commodity("TSX", "https://www.theglobeandmail.com/investing/markets/indices/", 17970.50)
	page = BeautifulSoup(requests.get(tsx.src).content, 'html.parser')
	raw = page.find("span", {"class": "barchart-overview-field-value"}).find("barchart-field").attrs['value']
	tsx.price = float(raw.replace(',',''))
	tsx.calcDiff()

	results = [dow, tsx]
	return results

results = scrape()
for c in results:
	c.print()