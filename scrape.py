from bs4 import BeautifulSoup
import requests

#scrape
page = requests.get("https://money.cnn.com/data/markets/dow/")
soup = BeautifulSoup(page.content, 'html.parser')
td = soup.find("td", {"class": "wsod_last wsod_lastIndex"})
spans = td.findAll("span")
price = float(spans[0].text.replace(',',''))
time = spans[1].text

#math
high52w = 29568.57
diff = high52w-price
diffPercent = (1-(price/high52w))*100

print("Current DOW: {0:.0f}".format(price))
print("Down {0:.0f} ({1:.0f}%) from 52-week high".format(diff, diffPercent))
print("Last updated: {0}".format(time))