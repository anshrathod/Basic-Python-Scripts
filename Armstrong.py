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
