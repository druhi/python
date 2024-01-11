num = 5 
for i in range(1,num+1):
    a = 1
    for j in range(i):
        print(a,end= "")
        a = 1 - a
    print()