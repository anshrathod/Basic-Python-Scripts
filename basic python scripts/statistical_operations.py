print("Enter the number")
num=int(input())

def sum(num):
    m=(num*(num+1))/2
    print("{0} is the sum of {1} natural numbers".format(m,num))
def mean(num):
    n=0
    for i in range(1,num+1):
        n=n+i
    p=n/num
    print("{0} is the mean of {1} natural numbers".format(p,num))
mean(num)
sum(num)
