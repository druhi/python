import random
counter = 0
with open("games.csv") as file:
    for line in file:
        ques, ans = line.rstrip().split(",")
        user_ans=input(f"{ques} ?").strip()
        if user_ans.casefold() == ans.casefold():
            print("Correct answer")
            counter=counter+1
        else:
            print("wrong answer")
print(f"Total score is {counter}")        