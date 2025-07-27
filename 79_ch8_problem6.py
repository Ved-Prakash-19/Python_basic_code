# write a python functions which converts inches to cms.

def inch_to_cms(inch):
    return inch * 2.54
# test the function

n = int(input("enter the number: "))
print(f"the corresponding value in cms is: {inch_to_cms(n)}")