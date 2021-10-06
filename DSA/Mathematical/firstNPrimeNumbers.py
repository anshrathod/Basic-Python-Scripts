# an efficient script to print the first n prime numbers
from math import sqrt

n = int(input("Enter a value for n: "))

# The num variable stores the number to be checked for primality.
num = 1

# count = 1 as num = 2 is accounted for.
count = 1

# 2 is the smallest prime number. It is also the only even prime.
print(2, end = ", ")

while True:
    # We'll check for odd nos. as the even nos. are divisible by 2, making them non-prime.
    num += 2

    # We'll check only for factors up to the square root of the no.
    for i in range(3, int(sqrt(num)), 2):
        if num % i == 0: break
    else:
        count += 1
        print(num, end = ", ")

    if count == n: break
