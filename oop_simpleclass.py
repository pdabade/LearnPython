class Person:
	def __init__(self,name):
		self.name = name
	def say_hi(self):
		print 'Hi '+ self.name +', how are you?'
	def say_hello(self):
		print 'Hello '+ self.name +', how are you?'
	
p = Person('Pooja')
p.say_hi()
p.say_hello()

#print p

