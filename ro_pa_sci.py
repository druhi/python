import getpass
choose1 = getpass.getpass('player 1 choose a opition(rock,paper,scissor or exit )').strip().casefold()
choose2 = getpass.getpass('player 2 choose a opition(rock,paper,scissor or exit )').strip().casefold()
# choose1 = input('player 1 choose a opition(rock,paper,scissor or exit )').strip().casefold()
# choose2 = input('player 2 choose a opition(rock,paper,scissor or exit )').strip().casefold()
#choose1 = input("player 1 choose a opition(rock,paper,scissor) ").strip().casefold()
word = ["rock","paper","scissor"]
#choose2 = input("player 2 choose a option(rock,paper,scissor) ").strip().casefold()
if choose1 and choose2 not in word:
     print("exiting")
     exit()
     
elif choose1 and choose2 == "exit":
     print("exiting")
     exit()

def game():
    points1 = 0
    points2 = 0

    if choose1 == "rock"and choose2 == "scissor":
        print(f"player 2 you lose {choose2} player 1 you won {choose1}")
        points1 += 1
    elif choose1 == "scissor"and choose2 == "rock":
        print(f"player 1 you lose {choose1} player 2 you won {choose2}")
        points2 += 1
    elif choose1 == "paper"and choose2 == "rock":
        print(f"player 2 you lose {choose2} player 1 you won {choose1}")
        points1 += 1
    elif choose1 == "rock"and choose2 == "paper":
        print(f"player 1 you lose {choose1} player 2 you won {choose2}")
        points2 += 1
    elif choose1 == "scissor"and choose2 == "rock":
        print(f"player 1 you lose {choose1} player 2 you won {choose2}")
        points2 += 1
    elif choose1 == "scissor"and choose2 == "rock":
        print(f"player 1 you lose {choose1} player 2 you won {choose2}")
        points2 += 1
    elif choose1 == "rock"and choose2 == "scissor":
        print(f"player 1 you lose {choose1} player 2 you won {choose2}")
        points2 += 1
    elif choose1 == choose2:
        print(f"its a tie of {choose1}")
    elif choose1 == "paper"and choose2 == "rock":
        print(f"player 1 you won {choose1} player 2 you lose {choose2}")
        points1 += 1
    elif choose1 == "rock"and choose2 == "paper":
        print(f"player 2 you won {choose2} player 1 you lose  {choose1}")
        points2 += 1
    elif choose1 == "scissor"and choose2 == "paper":
        print(f"player 1 you won {choose1} player 2 you lose {choose2}")
        points1 += 1
    elif choose1 == "paper"and choose2 == "scissor":
        print(f"player 1 you won {choose2} player 2 you lose {choose1}")
        points1 += 1
        if points1 > points2 :
            print("player 1 has won")
        elif points1 < points2 :
            print("player 2 has won")
        elif points1 == points2 :
            print("both have won")



def play():
    input("do you want to play more ")
    if "yes" :
        game()
    else:
        input 




game()
play()
