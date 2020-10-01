def binSearch(A, v):
    lo = 0
    hi = len(A)-1
    while (lo <= hi):
        mid = (lo+hi)//2
        if A[mid] == v:
            return mid
        else:
            if A[mid] < v:
                lo = mid+1
            else:
                hi = mid-1
    return -1

binSearch([1,2,3,5,6,9,12],6)