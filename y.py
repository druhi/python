import random
states1 = ["Andhra Pradesh","Arunachal Pradesh","UP",]
state = random.choice(states1)
a = input(f"what is the capital of {state} " ).lower().strip()
x = "Amravti"
y = "Itanagar"
z = "Lucknow"
if state == "Andhra Pradesh" and a == "amravati":
    print("correct")
elif state == "Arunachal Pradesh" and a == "itanagar":
        print("correct")
elif state == "UP" and a == "lucknow":
        print("correct")
else:
    print("incorrect")
