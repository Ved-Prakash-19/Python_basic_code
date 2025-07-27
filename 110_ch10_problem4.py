class calculator:
    def __init__(self, n):
        self.n = n
        
    def square(self):
        print(f"The square of this number is {self.n*self.n}")
        
    def cube(self):
        print(f"The cube of this number is {self.n*self.n*self.n}")
    
    def squareroot(self):
        print(f"The squareroot of this number is {self.n**0.5}")
        print(f"The squareroot of this number is {pow(self.n, 0.5)}")
        
    @staticmethod
    def hello():
        print("Hello there welcome to mathematics!")
        

a = calculator(25)
a.hello()
a.square()
a.cube()
a.squareroot()