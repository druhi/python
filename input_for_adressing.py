import random
import re
def ask():
    x2 = input("what is your name? ").strip()
    re.search(r"[0-9]", x2)
    y2 =    input("what is your age? ").strip()
    input("what is your e-mail? ").strip()
    print("thank you for playing my quiz ")
    quiz = ["is the process of a seed growing into a plant called gemination[yes/no] ","is the capital of bagladesh moscow?[yes/no] ","is africa the largest continenet?[yes/no] " , "chandrayaan 3 was indias moon mission"]
    random.choice(quiz)
    x = input(quiz[0])
    while  x not in ("yes","no") :
        print("plese choose yes or no")
        x = input(quiz[0])
    if x == "yes":
        print("correct")
    elif x == "no":
        print("wrong")
    y = input(quiz[1])
    while  y not in ("yes","no") :
        print("plese choose yes or no")
        y = input(quiz[1])
    if y == "no":
        print("Correct")
    elif y == "yes":
        print("Wrong")
    z = input(quiz[2])
    while  z not in ("yes","no") :
        print("plese choose yes or no")
        z = input(quiz[2])
    if z == "no":
        print("Correct")
    elif z == "yes":
        print("Wrong")
        w = input(quiz[3])
    while  w not in ("yes","no") :
        print("plese choose yes or no")
        w = input(quiz[3])
    if w == "no":
        print("Correct")
    elif w == "yes":
        print("Wrong")
    input("do you want to play again ")
    if "yes":
        ask()
    elif "no":
        print("exiting")
        exit()
def play_again():
    input("do you want to play again").strip()
    if "no":
        exit()

ask()
play_again()