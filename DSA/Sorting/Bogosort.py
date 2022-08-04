#sorting algorithm that uses randomness to sort a list
from random import sample

rando = [3,2,1,4,5,6,7]
count = 0
length = len(rando)

while True:
  if rando[count] < rando[count + 1]: # checking if the list is sorted
    count += 1
    if count + 1 == length:
      print(rando)
      exit()
  else:
    count = 0
    rando = sample(rando, length) # randomising the list
    #print(rando) -- Use this to see the solutions its trying
 #obviously this is not efficient. it lands in the horrible category of big o notation (O(n^2!))
