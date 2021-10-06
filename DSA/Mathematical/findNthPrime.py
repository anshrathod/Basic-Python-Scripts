# an efficient script to find the nth prime number
from math import sqrt

def nth_prime(n):
    # Since 2 is the smallest known even prime number.
    if n == 1:
        return 2

    # The num variable stores the number to be checked for primality.
    num = 1
    # count = 1 as num = 2 is accounted for.
    count = 1

    while True:
        # We'll check only for odd nos. as the even nos. are divisible by 2, making them non-prime.
        num += 2

        # We'll check only for factors up to the square root of the number.
        for i in range(3, int(sqrt(num)), 2):
            if num % i == 0:
                break
        else:
            count += 1
        if count == n:
            return num

nth_prime(int(input("Enter the value for n: ")))
