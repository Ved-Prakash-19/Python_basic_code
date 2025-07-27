# BREAK STATEMENT:--

for i in range (0,100):
    if (i == 50):
        break        #exit the loop right now.
    print(i)
    
#  CONTINUE STATEMENT:--

for i in range (0,100):
    if (i == 50):
        continue       #skip this loop iteration.
    print(i)
    

#PASS STATEMENT:--
#The pass statement in Python is a null operation — when it is executed, nothing happens. It
#can be used when a statement is required syntactically but no execution of code is necessary.
#The pass statement is also used as a placeholder when a function or a code block is incomplete.

for i in range(0,645):
    pass          # because of this pass condition below write code will be executed.
                  # OTHERWISE THIS CODE WILL NOT BE EXECUTED.


i = 0
while (i < 45):
    print(i)
    i = i + 1  # i+=1