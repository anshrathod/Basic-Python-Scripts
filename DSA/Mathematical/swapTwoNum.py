# Python program to swap two variables



a = input('Enter value of a: ')
b = input('Enter value of b: ')


temp = a
a = b
b = temp

print('The value of a after swapping: {}'.format(a))
print('The value of b after swapping: {}'.format(b))