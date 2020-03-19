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
		output = "{0},{1:.2f},{2:.2f},{3:.2f},{4:.2f}%,{5}".format(self.name, self.price, self.high52w, self.diff, self.diffPercent, self.time)
		return output