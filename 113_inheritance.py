class Employee:             # Base class
    company = "ITC"
    salary = 1200000
    language = "python"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary of Employee is {self.salary}")
        
'''class programmer:
    company = "ITC infotech"
    salary = 1200000
    language = "c++"
    def show(self):
        print(f"The name of the Programmer is {self.name} and the salary of Programmer is {self.salary}")
        
    def showlanguage(self):
        print(f"The name of the Employee is {self.name} and he knows {self.language} language")'''

class programmer(Employee):      #programmer ek class hai jisko mai Employee se inheritance kar raha hun  and  THIS IS CALLED INHERITANCE CLASS.
    company = "ITC infotech"
def showlanguage(self):
    print(f"The name of the Employee is {self.name} and he knows {self.language} language")
a = Employee()
b = programmer()

print(a.company,b.company, b.salary, b.language)



