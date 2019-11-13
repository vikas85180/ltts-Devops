# is subclass()  method program

class Base: #creating the base class
    def display(self):
        print("I am the base class")

class Derived(Base): # creating the derived class from the base class
    def display1(self):
        print("I am the Derived class")

obj = Derived()
print(issubclass(Derived, Base)) #using issubclass() method to check
