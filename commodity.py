class Commodity:
	name = ''
	src = ''
	price = 0
	high52w = 0
	diff = 0
	diffPercent = 0
	time = ''

	def __init__(self, name, src, high52w):
		self.name = name
		self.src = src
		self.high52w = high52w

	def calcDiff(self):
		self.diff = self.high52w-self.price
		self.diffPercent = (1-(self.price/self.high52w))*100

	def print(self):
		output = "{0} {1:.0f}; down {2:.0f} ({3:.0f}%) from 52W high".format(self.name, self.price, self.diff, self.diffPercent)
		if (self.time != ''):
			output += "; updated {0}".format(self.time)
		print(output)