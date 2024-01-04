import re
import random
def game():
    ask = input("Welcome to hangman : Enter Yes to start game ").strip().lower()
    if ask == "yes":
        print("lets start")
    else :
        print("exiting")
        exit()
    words = ["watch","rain","delhi","rainbow","tea","verb","europe","frog","ship","animal","lion","hat","dustbin","cow","pot","rat","can","train","odisha","goa","two","one","web","eat","put","ox","jar","bread","almond","walnut","peanut","dam","like","brazil","china","why","ass","brain","dry","cry","brinjal","rain","train","nail" ]

    word = random.choice(words)
    return word

def play_again():
    ask = input("do you want to play again : Yes/No ").strip().lower()
    if ask == "yes":
        print("Starting again")
        return True
    else :
        print("exiting")
        exit()



def hangman(word): 
    display = "_"*len(word)
    letters = list(word)
    guessed= []
    counter = 0
    limit = 5

    while counter < limit:
        guess = input(f"Hangman guess the word {display}: ").strip().lower()
        while len(guess) == 0 or len(guess) > 1 or re.search(r"[0-9~@#$^*()_+=[\]{}|\\,.?: -/].*",guess):
            print("Invalid input, please enter 1 word only")
            guess = input(f"Hangman guess the word {display}: ").strip().lower()
        if guess in guessed:
            print("Oops, you have already entered this letter, please enter other")
            continue
        if guess in letters:
            letters.remove(guess)
            index = word.find(guess)
            display = display[:index]+guess+display[index+1:]
        else:
            guessed.append(guess)
            counter +=1
            if counter == 1:
                print(f"wrong guess {limit-counter} guesses remaining")
                print('''  
   ____
  |    |      
  |    o     
  |   /|\    
  |    |
  |   / 
 _|_
|   |______
|          |
|__________|
                ''')
            elif counter == 2:
                print(f"wrong guess {limit-counter} guesses remaining")
                print('''  
   ____
  |    |      
  |    o     
  |   /|\    
  |    |
  |    
 _|_
|   |______
|          |
|__________|
                ''')
            elif counter == 3:
                print(f"wrong guess {limit-counter} guesses remaining")  
                print('''  
   ____
  |    |      
  |    o     
  |   /|   
  |    |
  |    
 _|_
|   |______
|          |
|__________|
                ''')              
            elif counter == 4:
                print(f"wrong guess. {limit-counter} guesses remaining")
                print('''  
   ____
  |    |      
  |    o     
  |    |   
  |    
  |    
 _|_
|   |______
|          |
|__________|
                ''')                
            elif counter == 5:
                print('''  
   ____
  |    |      
  |         
  |       
  |    
  |    
 _|_
|   |______
|          |
|__________|
                ''')
                print(f"wrong guess {limit-counter} guesses remaining, You loose! The word was {word}")
        if display == word:
            print(f"Congrats! you have guessed the word {word} correctly")
            break


def main():
    word = game()
    hangman(word)
    playagain = play_again()
    while playagain:
        word = game()
        hangman(word)
        playagain = play_again()

main()
    
