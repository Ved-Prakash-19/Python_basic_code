class Employee:
    salary = "111000000"
    language = "python"           # this is class attributes.
    
    def __init__(self , name, salary, language):    # This is a dunder method which is automatically called.
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating an object")
        
gaurav = Employee("gaurav", 100000000, "c++")   # this is called instance attributes.
# gaurav.name = "gaurav"
# gaurav.language = "c++"    
print(gaurav.name, gaurav.salary, gaurav.language)

# ved = Employee()

# __init__ dunder method which is automatically called.and it is special method which is first run as soon as the object is created. and this method is also known as constructor.
# it takes 'self' arguments and can also takes further arguments.