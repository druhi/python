name = input("what is your name ")
file = open("names.csv" , "a")
file.write(f"{name}\n")
file.close()

with open("names.csv", "r") as file:
    lines = file.readlines()
for line in lines:
    print("hello, ",line.rstrip())

