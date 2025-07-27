'''sometimes we need a function that does not  use the self parameter. then we can defi ne a static method like this.'''

# self parameter :-

class Employee:
    def greet(self):
        print("Hello, my name is ved prakash")
        
vedprakash = Employee()
vedprakash.greet()

# This is self parameter method.

# STATIC METHOD:-
class Employee:
    
    @staticmethod
    def greet():
        print("Hello, my name is ved prakash")
        
vedprakash = Employee()
vedprakash.greet()

# here greet is a static method and it doesnt need object.(self)