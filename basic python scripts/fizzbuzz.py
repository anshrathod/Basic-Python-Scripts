""" Prints Fizz when number divisible by Three.
    Prints Buzz when number divisible by Five.
    Prints FizzBuzz when number divisible by Three and Five.
    Else Prints the Actual Number

    Example: if Number = 3 Then Fizz
             if Number = 5 Then Buzz
             if Number = 15 Then FizzBuzz
             If Number = 7 Then 7
"""
def fizz_buzz(num):
    output = ""
    if num % 3 == 0:
        output += 'Fizz'
    elif num % 5 == 0:
        output += 'Buzz'
    else:
        output = num
    print(output)

for i in range(1, 100):
    fizz_buzz(i)

# List Comprehension
# [fizz_buzz(i) for i in range(1, 100)]
