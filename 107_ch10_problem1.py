class programmer:
    company = "microsoft"
    salary = 12000000
    
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
gaurav = programmer("gaurav", 100000000, 811315)
print(gaurav.name, gaurav.salary, gaurav.pin, gaurav.company)

ved = programmer("ved", 10000000, 811311)
print(ved.name, ved.salary, ved.pin, ved.company)
