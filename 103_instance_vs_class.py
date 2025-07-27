class Employee:
    language = "python"  #this is a class attribute
    salary = "10000000"
    
gaurav = Employee()
gaurav.language = "c++"
print(gaurav.language, gaurav.salary)  

# instance attributes , take preference over class attributes during assingnment and retrievals 