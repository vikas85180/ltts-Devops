#Basic Inhritance Program
class Human: #creating base Class
	def Speaks(self):
		print("vikas speaks about DevOps")

		
class Human_Listeners(Human): #creating Derived class
	def listen(self):
		print("And Others Listen")

obj1 = Human_Listeners()
obj1.Speaks()
obj1.listen()
