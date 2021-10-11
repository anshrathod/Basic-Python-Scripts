#to find frequency count of a item in a list
list1=[1,2,3,5,3,6,4,1,2,11,2,3,1,4,5]
cnt=0
freqcountof=1                   # value of item to b counted
for i in range (0,len(list1)):
    if list1[i]==freqcountof:
        cnt+=1
print("Count of ",freqcountof," in ",list1," is ",cnt)
# Alternatively print(list1.count(freqcountof)) would also give the same result.    