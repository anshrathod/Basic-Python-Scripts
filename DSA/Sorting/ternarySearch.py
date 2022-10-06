"""
Ternary Search|

We can divide the array into three parts by
taking mid1 and mid2 which can be calculated
as shown below. Initially, l and r will be
equal to 0 and n-1 respectively, where n is
the length of the array.
mid1 = l + (r-l)/3
mid2 = r – (r-l)/3
"""
def ternerySearch(arr,x):
    l=0
    r=len(arr)-1
    while l<=r:
        m1= l+(r-l)//3
        m2 = r-(r-l)//3
        if x<arr[m1]:
            r=m1-1
        elif x>arr[m2]:
            l=m2+1
        elif x==arr[m1] or x==arr[m2]:
            return True
        else:
            l=m1+1
            r=m2-1
    return False


"""
We can apply ternery search on unimodal
functions:-
    A function f(x) is a unimodal function
    if for some value m, it is monotonically
    increasing for x ≤ m and monotonically
    decreasing for x ≥ m.
"""
