class gaurav:
    a = 5
    
object = gaurav()
print(object.a)          #Print the class attributes because instance attributes is not present.   (instance attributes >> class attributes )

object.a = 0             # instance attributes is set here
print(object.a)          #so print instance attributes because it is present.

print(gaurav.a)    # This is class attributes 