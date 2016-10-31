class wholesale(object):
	def _init_(self,amount,item,price,networth=15000):
		self.amount=amount
		self.item=item
		self.price=price
	
	def selling(self,amount):
		self.Balance = (amount)
	def buying (self,amount):
		if (self.Balance - amount < - networth):
			return False
		else:
			self.Balance  -=amount
			return True

	def balance(self):
		return self.Balance
