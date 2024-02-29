import random
states1 = ["Andhra Pradesh","Arunachal Pradesh","UP",]
state = random.choice(states1)
a = input(f"what is the capital of {state} " )
x = "Amravti"
y = "Itanagar"
z = "Lucknow"
if state == "Andhra Pradesh" and a == "Amravati":
    print("correct")
elif state == "Arunachal Pradesh" and a == "Itangar":
        print("correct")
elif state == "UP" and a == "Lucknow":
        print("correct")
else:
    print("incorrect")

