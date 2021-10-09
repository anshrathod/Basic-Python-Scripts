def factorial(num):
    if num ==0 or num==1:
        return 1
    else:
        return num * factorial(num - 1)
    
n=int(input("Enter a Non-Negative Integer : "))
print(n,"! is ",factorial(n),sep="")
