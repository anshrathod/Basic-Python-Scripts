string=input('enter any string : ')
print(type(string))
n=len(string) 
left=0
right=n-1
str_copy=[c for c in string]
def permutation(string,left,right):
    if str_copy[left]==str_copy[right]: 
        print("".join(str_copy))
    else: 
        for i in range(left,right+1): 
            temp=str_copy[left]
            str_copy[left]=str_copy[i]
            str_copy[i]=temp
            permutation(string,left+1,right) 
            temp=str_copy[left]
            str_copy[left]=str_copy[i]
            str_copy[i]=temp
    return 
permutation(string,0,n-1)
