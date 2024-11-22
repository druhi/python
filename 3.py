n = 5
a = 65
for i in range(1,n+1):
    for j in range(0,i):
        print(chr(a), end= "")
    print()
    a += 1