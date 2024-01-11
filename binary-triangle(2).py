num = 5
for i in range(1,num+1):
    if (i%2) == 0:
        a= 1
    else:
        a =0
    for j in range(i):
        print(a, end = "")
        a = 1 - a
    print()
