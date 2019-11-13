#Method Overrriding

class SeniorEngineer: #Base class
    def display(self): #Base class function
        print("senior engineer function can be overridden by specialist")

class Specialist(SeniorEngineer): #derived class
    def display(self): #derived class function named same as base class function
        print("specialist function override the SE function")

obj = Specialist()
obj.display()
