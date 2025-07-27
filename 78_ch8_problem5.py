def pattern(n):
    if(n == 0):
        return              #it means stop.
    print("*" * n)
    pattern(n-1)
    
n = int(input("enter the number: "))
print(pattern(n))