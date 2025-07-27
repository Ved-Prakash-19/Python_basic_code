def multiply(n):
    for i in range(0, 11):
        print(f"{n} * {i} = {n * i}")
        
n = int(input("Enter the number which you want to table: "))
print(multiply(n))
