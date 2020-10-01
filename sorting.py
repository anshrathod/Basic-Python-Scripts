import datetime
start = datetime.datetime.now()
arr = [5, 8, 1, 3, 3, 0, 7, 4,5,8, 9, 10, 84, 34, 22]
arr_size = len(arr)
new_arr = [None]*(arr_size)
n = 0

for i in range(arr_size):
    n=0
    for j in range(arr_size):
        if arr[i] > arr[j]:
            n+=1
    while new_arr[n] == arr[i]:
        n+=1
    new_arr[n] = arr[i]

arr = new_arr

for i in range(arr_size): 
    print ("%d" %arr[i]), 

finish = datetime.datetime.now()
print (finish-start)
