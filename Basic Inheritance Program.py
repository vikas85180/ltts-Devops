Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Human:
	def Speaks(self):
		print("vikas speaks about DevOps")

		
>>> class Human_Listeners(Human):
	def listen(self):
		print("And Others Listen")

		
>>> obj1 = Human_listeners()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    obj1 = Human_listeners()
NameError: name 'Human_listeners' is not defined
>>> obj1 = Human_Listeners()
>>> obj1.speaks()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    obj1.speaks()
AttributeError: 'Human_Listeners' object has no attribute 'speaks'
>>> obj1.Speaks()
vikas speaks about DevOps
>>> obj1.listen()
And Others Listen
>>> 
