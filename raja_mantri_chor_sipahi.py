import random

word = ["raja","mantri","chor","sipahi"]
player1= []
player2 = []

def name():
        team1 = input("Player1 please enter your name: ").strip()
        team2 = input("Player2 please enter you name: ").strip()
        return(team1,team2)
      

def game(team1,team2):
        # team1 = input("Player1 please enter your name: ").strip()
        # team2 = input("Player2 please enter you name: ").strip()
        input(f"{team1},press enter to pick a slip ")
        choose = random.choice(word)
        if choose == "raja":
            print("Congrats! You have picked Raja 🤴 and scored 3 points")
            player1.append(int(3))
        elif choose == "mantri":
            player1.append(int(2))
            print("good one! You have picked Mantri 👨‍💼 and scored 2 points")
        elif choose == "chor":
            player1.append(int(0)) 
            print("bad luck! You have picked Chor 🦹 and scored 0 points")                          
        elif choose == "sipahi":
            player1.append(int(1))
            print("well try! You have picked Sipahi 👮 and scored 1 points")
        input(f"{team2}, press enter to pick a slip ")
        choose = random.choice(word)
        if choose == "raja":
                print("Congrats! You have picked Raja 🤴 and scored 3 points")
                player2.append(int(3))
        elif choose == "mantri":
                player2.append(int(2))
                print("good one! You have picked Mantri 👨‍💼 and scored 2 points")
        elif choose == "chor":
                player2.append(int(0)) 
                print("bad luck! You have picked Chor 🦹‍♂️ and scored 0 points")                          
        elif choose == "sipahi":
                player2.append(int(1))
                print("well try! You have picked Sipahi 👮 and scored 1 points")

def play_again(team1, team2):
    ask = input("do you want to play again : Yes/No ").strip().lower()
    if ask == "yes":
        return True
    else :
        ask = input("Are you sure you do not want to play? : Yes/No ").strip().lower()
        if ask == "yes":
              return True
        else:      
             score1 = 0
             for i in range(0,len(player1)):
              score1 = score1 + player1[i]
             score2 = 0
             for i in range(0,len(player2)):
              score2 = score2 + player2[i]   
             if score1 == score2:
              print(f"Its a draw match with {score1} points each!")    
             elif score1 > score2:
              print(f"{team1} you have won, your score is {score1}, {team2} you scored {score2} only!") 
             else:
              print(f"{team2} you have won, your score is {score2}, {team1} you scored {score1} only!")                  
        print("exiting, Thanks for playing the game")
        exit()        


def main():
    team1, team2 = name()
    game(team1, team2)
    playagain = play_again(team1, team2)
    while playagain:
            game(team1, team2)
            playagain = play_again(team1, team2)
    
main()

    




