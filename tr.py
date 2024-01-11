num = 5
for i in range(0,num):
    for j in range(0,i):
        print(" ", end= " ")
    for k in range(0,(2*(num-i)-1)):
        print("^", end= " ")
    print()