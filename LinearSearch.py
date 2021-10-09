def sortedSearch(A, v):
    for i in range(len(A)):
        if A[i] == v:
            return i
        if A[i] > v:
            return -1
    return -1

sortedSearch([1,2,3,5,6,9,12],6)


# Above code complexity will be O(n) if  List is  sorted 
# Linear Search Complexity should  O(n) whether it's sorted or not

def linearSearch(mylist,key):
    for index in range(len(mylist)):
        if mylist[index]==key:
            return index
    return -1

print(linearSearch([1,2,3,5,6,9,12],6))
