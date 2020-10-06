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