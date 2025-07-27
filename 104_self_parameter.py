class Employee:
    language = "python"  #this is a class attribute
    salary = "10000000"

    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")
        
    def greet(self):
        print("good morning")
        
gaurav = Employee()  #This line creates an instance of the Employee class named gaurav.
gaurav.language = "c++"
print(gaurav.language, gaurav.salary)
  
gaurav.getInfo()
# Employee.getInfo(gaurav)

gaurav.greet()
# Employee.greet(gaurav)



'''The self Parameter
The self parameter in Python is a reference to the current instance of the class. It is used to access variables that belong to the class.
When you define a method within a class, the first parameter must be self'''