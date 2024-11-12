
x = int(input("till which numbers table you want"))
y = 1
w = 2
for w in range(2,x+1):
    for Y in range(10):
       z = w*y
       print(f"{w}*{y}={z}")
       y=y+1
       if y == 11:
          y = 1        
    print("\t")      
    w=w+1



