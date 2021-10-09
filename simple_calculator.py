#Simple Calculator

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("For Exit, press any integer >4 or <1")
choice = int(input("Enter Choice "))
if choice in [1,2,3,4] :
    num1 = int(input("First Number : "))
    num2 = int(input("Second Number : "))
    if choice ==1:
        res = num1 + num2
        print("Sum: ", res)
    elif choice == 2:
            res = num1 - num2
            print("Difference:",res)
    elif choice==3:
            res=num1*num2
            print("Product:",res)
    else:
        if num2==0:
            print("Division by Zero Error")
        else:
            res=num1//num2
            print("Quotient:",res)
