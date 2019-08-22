# Question 8:

# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

class iterator:
	"""
	Generator generates numbers from 0 to n 
	Returns:
		Numbers divisible by 7
	"""
	def __init__(self, n):

		"""
			Initialize the constructor				
		"""
		super(iterator, self).__init__()
		self.n = n
		
	def divBySeven(self):

		"""
			Generates numbers divisible by 7 within given range n
			Returns:
				Numbers divisible by 7
		"""

		for i in range(0, self.n):
			if i % 7 == 0:
				yield i
n = int(input("Enter the number: "))
for num in iterator(n).divBySeven():
	print (num, end="")