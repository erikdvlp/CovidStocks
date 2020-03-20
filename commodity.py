class Commodity:
	name = ''
	src = ''
	price = 0
	high52w = 0
	diff = 0
	diffPercent = 0
	time = ''
	upDown = ''

	def __init__(self, name, src, high52w):
		self.name = name
		self.src = src
		self.high52w = high52w

	def calcDiff(self):
		self.diff = abs(self.high52w-self.price)
		self.diffPercent = abs((1-(self.price/self.high52w))*100)
		if (self.price >= self.high52w):
			self.upDown = 'Up'
		else:
			self.upDown = 'Down'

	def format(self):
		self.price = "{0:.0f}".format(self.price)
		self.diff = "{0:.0f}".format(self.diff)
		self.diffPercent = "{0:.0f}%".format(self.diffPercent)