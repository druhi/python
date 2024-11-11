import getpass
one = getpass.getpass((" play 1 rock paper scisor or exit :"))
two = getpass.getpass((" play 2 rock paper scisor or exit :"))
print("shoot")
if one == "rock" and two == "paper":
    print("player 2 wins (paper)")
elif one == "paper" and two == "rock":
    print("player 1 wins (paper)")
elif one == "scissor" and two == "rock":
    print("player 2 wins (rock)")
elif one == "rock" and two == "scissor":
    print("player 1 wins (rock)")
elif one == "scissor" and two == "paper":
    print("player 1 wins (scissor)")
elif one == "paper" and two == "scissor":
    print("player 2 wins (scissor)")
elif one or two == "exit":
    exit()
