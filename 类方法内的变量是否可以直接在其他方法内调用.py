class A:
	def __init__(self):
		for i in self.console():
			self.a1=i
			self.out()
	def console(self):
		for i in range(2):
			print(self.b1)
			yield i
	def out(self):
		self.b1=2
		print(self.a1)
obj = A()
print(obj)