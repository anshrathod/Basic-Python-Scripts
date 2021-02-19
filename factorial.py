# example of a recursive function.
def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result

print(factorial(7))
