import random
counter = 0
game = []
with open("games.csv") as file:
    for line in file:
        ques, ans = line.rstrip().split(",")
        games = {"key": ques, "value": ans}
        game.append(games)

# print(game[0])
# print(game[1])
for games in game:
    print(f"{games['key']}")
