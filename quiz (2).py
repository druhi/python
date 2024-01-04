import re
import random
def game():
    name1 = input(" player 1 what is your name : ").strip()
    counter = 1
    while re.search(r"[0-9]", name1): 

         if counter == 3 :
              print("3 times wrong input, exiting")
              exit()         
         counter = counter + 1
         name1 = input(" invailid name , please enter your own name : ").strip()
    print(f"hello {name1},")     


def play():   
    word = ["is the capital of france paris (yes/no) : ","is the capital of bagladesh delhi (yes/no) ","is the capital of england beijing (yes/no) : ","is the capital of russia moscow (yes/no) : "]
    random.shuffle(word)
    random.choice(word)
    x = input(word[0]).strip().lower()
    print(x)
    while x not in ("yes","no"):
         print("enter again")
         x = input(word[0]).strip().lower()
    if x == "yes":
            print("Ans 1 incorrect")
    elif x == "no":
        print("Ans 1 correct")     
    y = input(word[1])
    print(y) 
    z = input(word[2])
    print(z)
    w = input(word[3])
    print(w)
    if x == "yes":
            print("Ans 1 correct")
    elif x == "no":
        print("Ans 1 wrong")
    if  y ==  "no":
        print("Ans 2 correct")
    elif y == "yes":
         print("Ans 2 is wrong")
         if z == "no":
              print("ans 3 correct")
    elif z == "yes":
              print("ans 3 wrong")
    elif w == "yes":
         print("ans 4 correct")
    elif w == "no":
         print("ans 4 wrong")
                   
    

       
                
         
def main():
    game()
    play()
main()

