num = int(input("Enter a number : "))
fact = 1
if num < 0:
    print("Factorial of",num,"does not exist")
elif num == 0:
    print("Factorial of",num,"is",fact)
else:
    for i in range(1,num+1):
        fact = fact * i
    print("The factorial of",num,"is",fact)
    
