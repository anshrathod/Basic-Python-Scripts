#Easy python script to generate all the substringss of a given string
test_str='HELLO'
#res is a list(list-->[])
res = [test_str[i: j] for i in range(len(test_str))                        #splits the  test_str and copies it into result as list
          for j in range(i + 1, len(test_str) + 1)] 
print(res)