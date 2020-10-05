# python script to determine if a number is Armstrong number or not.
def is_Armstrong_number(num):

    # No. of digits in the number becomes the power to be raised for each digit
    n = len(str(num))

    # variable to store the sum of the digits raised to the nth power.
    total = 0

    temp = num
    while temp > 0:
        rem = temp % 10
        total += rem**n
        temp //= 10

    if total == num:
        return True
    return False

num = int(input())
if is_Armstrong_number(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
