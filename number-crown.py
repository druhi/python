num = 5
for i in range(1,num+1):
        a = 1
        for j in range(0,i):
            print(a, end = "")
            a += 1
        for k in range(0,2*(num-i)):
            print(" ", end = "")
        for l in range(0,i):
            print(i, end = "") 
            i = i - 1
        print()
        

