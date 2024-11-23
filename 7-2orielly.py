import random
ask = input("how many people are there - ")
r = ["1","2","3","4","5"]
if ask >= "8":
    print("you will have to wait for a table")
else:
     print(f"table no {random.choice(r)}")