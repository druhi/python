import random
num = random.randint(0,50)

while(True):
    ask = int(input(" whats the number : "))
    if ask > 50:
        print("sorry the number is above limit, exiting")
        exit()
    elif ask > num:
        print(f"it is smaller than {ask}")
    elif  ask < num:
        print(f"it is bigger than {ask}")
    elif ask == num:
        print(" congrats! you win")
    break

