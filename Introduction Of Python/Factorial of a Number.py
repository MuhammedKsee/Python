num = int(input("Please enter a number : "))

fact = 1
for a in range(1,num+1):
    fact *=a
print("The factorial of",num,"is",fact)