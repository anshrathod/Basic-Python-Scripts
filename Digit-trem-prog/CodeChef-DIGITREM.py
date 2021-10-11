# digit input function
def dinput():
    while True:
        d = int(input('\nenter the unwanted digit:'))
        if d >= 0 & d <= 9:
            break
    return d

# number input function


def ninput():
    while True:
        n = int(input('enter the number:'))
        if n >= 1:
            break
    return n

# Split number into a list of integers


def intsplit(x):
    digitlist = []
    for i1 in range(len(x)):
        digitlist.append(int(x[i1]))
    return digitlist


listofdigits = []
# input of number of cases with basic verification
while True:
    T = int(input('enter number of test cases:'))
    if T >= 1:
        break
# first "for" iteration for the number of tests
for i in range(T):
    N = ninput()
    D = dinput()
    N1 = N
    listofdigits = intsplit(str(N))
    sum1 = 0
    # here is where the search and destroy is done
    while True:
        if listofdigits.count(D) == 0:
            break
        else:
            sum1 = sum1 + 1
            N1 = N1 + 1
            listofdigits = intsplit(str(N1))
    # here printing the results , rinse and repeat
    print("you should add ", sum1, "to ", N, "to have ", N1, "which doesn't have the unlucky chosen digit", D, "\n")
