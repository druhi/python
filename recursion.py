from itertools import count
def recursion (count):
 if count == 5:
     return 0
 else :
     print("hello world",count)
 recursion(count + 1)
count = 1
recursion(count)