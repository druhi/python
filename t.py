name = input("what is your name ")
age = input("what is your age ")
if age == 9 :
    print("your big so you cant join in the quiz")
else:
    ask = input("do you want to play ")
    if ask == "no":
        exit()
    else:
        ans1 = input("which is the largest continent (africa / asia)" )
        if ans1 == "asia":
            print(f"correct {name} the largest continent is asia")
        else:
            print(f"wrong {name} the largest continent is asia")
            ans2 = input("which is the smallest continent ( austrilia / asia)")
    if ans2 == "asia":
       print(f"wrong {name} the largest continent is asia")
    else:
        print(f"correct {name} the smallest continent is austrilia")



