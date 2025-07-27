a = "5.6"
b = float(a)   # A but the type should be float
t = type(b)
print(t)

a = 31
b = str(a)
t = type(b)
print(t)

a = "31"
b = int(a)
t = type(b)
print(t)

a = str(31)
b = int(31)
t = type(b)
print(t)
