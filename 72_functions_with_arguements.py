def goodday(name, ending):
    print("Good day! " + name)
    print(ending)
    
goodday("ved prakash", "Thank you")
goodday("sagar satyarth", "Thank you")
goodday("gaurav singh", "Thanks")


def goodday(name, ending):
    print("Good day! " + name)
    print(ending)
    return "ok"           #return value of functions. kisi variable ko diya jata hai.

a = goodday("ved prakash", "Thank you")     # a = variables 
print(a)