n = int(input("enter the number:"))

product = 1
for i in range(1 ,n+1):
    product = product*i
print(f"the factorial of {n} is {product}")

print("The factorial of " + str(n) + " is " + str(product))