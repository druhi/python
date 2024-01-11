num = 5

def tri():
    for i in range(1,num+1):
        for j in range(0,2*(num-i)):
            print(" ", end = "")
        for k in range(0,2*i-1):
            print("^", end= " ")
        print()

def invtri():
    for i in range(0,num):
        for j in range(0,i):
            print(" ", end = " ")
        for k in range(0,(2*(num-i)-1)):
            print("^", end= " ")
        print()

tri()
invtri()