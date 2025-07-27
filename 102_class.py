class Employee:
    language = "python"
    salary = "10000000"
    
ved = Employee()
ved.name = "ved"
print(ved.name, ved.language, ved.salary)

gaurav = Employee()
gaurav.name = "gaurav"
print(gaurav.name, gaurav.language, gaurav.salary)

# here name is instance attribute and salary and language are class atrribute as they directly belong to class..