# python script to find factorial of a number
num = int(input("Enter a number : "))
fact = 1
#  negative numbers doesn't hhave factorial
if num < 0:
    print("Factorial of", num, "does not exist")
else:
    #product of numbers from 1 -> num-1 is calculated
    for i in range(1, num+1):
        fact = fact * i
    print("The factorial of", num, "is", fact)
