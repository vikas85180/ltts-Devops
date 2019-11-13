#Basic class and object program
class Employee: #creating class
    id = 1;
    name = "vikas sharma";
    def display(self):
        print("ID = %d \n Name: %s" %(self.id, self.name))
emp1 = Employee() #creating Object
emp1.display() #calling through object

