def sortedSearch(A, v):
    for i in range(len(A)):
        if A[i] == v:
            return i
        if A[i] > v:
            return -1
    return -1

sortedSearch([1,2,3,5,6,9,12],6)