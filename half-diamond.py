def triangle():
    num = 5
    for i in range(num):
        for j in range(i):
                print("^", end = "")
        print()
def invtriangle():
    num = 5
    for i in range(num):
        for j in range(num-i-2):
                print("^", end = "")
        print()
triangle()
invtriangle()

                