import random

states1 = {
  "UP": "Lucknow",
  "AP": "Itanagar",
  "MP": "Bhopal"
}

res = key, val = random.choice(list(states1.items()))

a = input(f"what is the capital of {key} " ).strip().lower()

if key == "AP" and a == "itanagar":
    print("correct")
elif key == "UP" and a == "lucknow":
        print("correct")
elif key == "MP" and a == "bhopal":
        print("correct")
else:
    print(f"incorrect, Ans is {val}")
