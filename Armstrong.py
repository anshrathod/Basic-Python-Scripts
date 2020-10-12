
# Function to calculate order of the number
def order(x):

    # Variable to store of the number
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10

    return n

# Function to check whether the given
# number is Armstrong number or not


def check_Armstrong(x):

    sum1 = 0
    temp = x
    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + r**3
        temp = temp // 10

    return (sum1)


n = int(input("Enter Numer"))
ans = check_Armstrong(n)

if(ans == n):
    print(n, "is an armstong number")
else:
    print(n, "is NOT an armstong number")
