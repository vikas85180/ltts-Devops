#multiple inheritance

class Immediate_S:#first base class
    def display(self):
        print("IS is a specialist")

class Mentor: #Second base class
    def display1(self):
        print("Mentor is a senior engineer")

class Associate_E: #third base class
    def display2(self):
        print("Associate engineers are new learners")

class Team(Immediate_S, Mentor, Associate_E): #derived class
    def display3(self):
        print("TOGETHER THEY ARE A TEAM")

obj1 = Team()
obj1.display()
obj1.display1()
obj1.display2()
obj1.display3()
