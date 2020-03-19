import os
import sys
from bs4 import BeautifulSoup
import requests as r
import commodity as c

sys.path.insert(0, os.path.dirname(__file__))

def scrape():
	#DOW
	dow = c.Commodity("DOW", "https://money.cnn.com/data/markets/dow/", 29568.57)
	page = BeautifulSoup(r.get(dow.src).content, 'html.parser')
	raw = page.find("td", {"class": "wsod_last wsod_lastIndex"}).findAll("span")
	dow.price = float(raw[0].text.replace(',',''))
	dow.time = raw[1].text[:-3]
	dow.calcDiff()

	#TSX
	tsx = c.Commodity("TSX", "https://www.theglobeandmail.com/investing/markets/indices/", 17970.50)
	page = BeautifulSoup(r.get(tsx.src).content, 'html.parser')
	raw = page.find("span", {"class": "barchart-overview-field-value"}).find("barchart-field").attrs['value']
	tsx.price = float(raw.replace(',',''))
	tsx.calcDiff()

	results = [dow, tsx]
	return results

def processResults(results):
	output = ""
	for result in results:
		output += result.print()
		output += "\n"
	return output

def run(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    results = scrape()
    output = processResults(results)
    return [output.encode()]