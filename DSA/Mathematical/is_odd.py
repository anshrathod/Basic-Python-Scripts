def is_odd(val):
    if type(val) is not int:
        raise TypeError('Typeof val must be int')

    return val & 1

try:
    print(is_odd('hello'))
except:
    pass

print(is_odd(1))
print(is_odd(2))
