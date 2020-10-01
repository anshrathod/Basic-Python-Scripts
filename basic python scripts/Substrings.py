#Easy python script to generate all the substringss of a given string
teststring='HELLO'
#res is a list(list-->[])
res = [teststring[i: j] for i in range(len(teststring))                        #splits the  test_str and copies it into result as list
          for j in range(i + 1, len(teststring) + 1)] 
print(res)