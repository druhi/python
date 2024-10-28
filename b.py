
while (True):
    movie_ticket = int(input("age :"))
    if movie_ticket < 3:
        print("your ticket is free")
    elif  3 < movie_ticket < 12:
        print("your ticket is 10")
    elif movie_ticket > 12:
        print("your ticket is 15")
    ask = input("press N to quit")
    if ask == "N".lower().strip():
        print ("exit")
        exit()