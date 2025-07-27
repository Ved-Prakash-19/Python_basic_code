class Employee:
    company = "ITC infotech"
    name = "Ved Prakash"
    def show(self):
        print(f"The name of the Employee is {self.name} and The name of the company is {self.company}")
        
class coder:
    language = "python"
    def printlangauges(self):
        print(f"The language of the coder is {self.language}")
        
        
        
class programmer(Employee, coder):      # Multiple inheritance
    company = "google"
    def showlanguage(self):
        print(f"the name of the company is {self.company} and the language of coder is {self.language}")
        
a = Employee()
b = programmer()

b.show()
b.printlangauges()
b.showlanguage()