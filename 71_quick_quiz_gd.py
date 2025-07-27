def goodday(name, ending = "thank you"):
    print(f"Good day!, {name}")
    print(ending)
    
    #DEFAULT PARAMETER VALUE:---
    
goodday("ved prakash","thanks")       #updated value = thanks.then print thanks.


#2nd method:--

def goodday(name, ending):
    print(f"Good day!, {name}")
    print(ending)
    
goodday("ved prakash", "thank you")