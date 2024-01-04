import random
color = input("tipi tipi top which colour do you want(choose a colour from the option) - red 🔴   yellow 🟡   green 🟢   blue 🔵 ")
num = input("tipi tipi top which number do you want(choose a number from the option) - 1  5  7  9 ")
word = "icy cold 🧊","great queen 🤴","loosing looser 😃","amazing choice 🤩 "
random.choice(word)

colour = ["red","yellow","green","blue"]
number = ["1","5","7","9"]
if color not in colour or num not in number:
    print("your option is not in my option list, sorry exiting")
    exit()
else: 
    print(random.choice(word))

